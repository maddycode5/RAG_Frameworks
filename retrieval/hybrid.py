"""
Purpose:
    Performs Hybrid Retrieval using
    Dense Retrieval + Sparse Retrieval + RRF.

Workflow

Query
    ↓
Dense Retriever
    ↓
Sparse Retriever
    ↓
Reciprocal Rank Fusion
    ↓
Hybrid Results
"""

from typing import List
from retrieval.base import BaseRetriever
from retrieval.dense import DenseRetriever
from retrieval.sparse import SparseRetriever
from retrieval.rrf import ReciprocalRankFusion

from core.retrieval_result import RetrievalResult

from utils.logger import logger
from config import TOP_K 
from concurrent.futures import ThreadPoolExecutor

class HybridRetriever(BaseRetriever):
    def __init__(
            self,
            dense_retriever :DenseRetriever,
            sparse_retriever : SparseRetriever,
            rrf : ReciprocalRankFusion,
    ):

        self.dense = dense_retriever
        self.sparse =sparse_retriever
        self.rrf =rrf

    def retrieve(
            self,
            query:str,
            top_k :int =TOP_K,
    ) -> List[RetrievalResult]:

        logger.info("Hybrid Retrieval starting")


        with ThreadPoolExecutor(max_workers =2) as executor:
            dense_future =executor.submit(self.dense.retrieve,query,top_k)
            sparse_future = executor.submit(self.sparse.retrieve,query,top_k)

            dense_results = dense_future.result()
            sparse_results = sparse_future.result()


        # """
        #  DENSE RETRIEVAL
        # dense_results = self.dense.retrieve(
        #     query =query,
        #     top_k = top_k,
        # )

        # # SPARSE RETRIEVER 
        # sparse_results = self.sparse.retrieve(
        #     query=query,
        #     top_k=top_k,
        # )

        # """
        #   RRF
        hybrid_results = self.rrf.fuse(
            dense_results,
            sparse_results
        )

        logger.info(
            f"Hybrid Retriever Returned{len(hybrid_results)} chunks "
        )

        return hybrid_results
    