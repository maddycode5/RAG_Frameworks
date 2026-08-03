"""
Purpose:
    Public retrieval interface for the framework.

Responsibilities:
    - Select retrieval strategy.
    - Delegate retrieval.
    - Hide implementation details.
"""
from typing import List
from config import(
    RETRIEVAL_TYPE,
    TOP_K,
)
from core.retrieval_result import RetrievalResult
from retrieval.dense import DenseRetriever
from retrieval.sparse import SparseRetriever
from retrieval.rrf import ReciprocalRankFusion
from retrieval.hybrid import HybridRetriever

from vectordb.manager import IndexManager

from utils.logger import logger

class Retriever:
    def __init__(self,manager:IndexManager):
        self.manager =manager,
        self.strategy =self._initialize_strategy()

    # Initialize Retrieval Strategy

    def _initialize_strategy(self):
        repository = self.manager.get_repository()

        if RETRIEVAL_TYPE == "dense":
            logger.info("Using Dense Retriever")

            return DenseRetriever(
                faiss_store=self.manager.get_faiss_store(),
                repository =repository,
            )

        elif RETRIEVAL_TYPE =="sparse":
            logger.info("Uisng SPARSE Retriever")
            return SparseRetriever(
                bm25_store = self.manager.get_bm25_store(),
                repository =repository,
            )

        elif RETRIEVAL_TYPE == "hybrid":
            logger.info("Using Hybrid Retriever")

            dense = DenseRetriever(
                faiss_store=self.manager.get_faiss_store(),
                repository =repository,
            )

            sparse = SparseRetriever(
                bm25_store=self.manager.get_bm25store(),
                repository=repository,
            )

            return HybridRetriever(dense_retriever=dense,
                                   sparse_retriever=sparse,
                                   rrf =ReciprocalRankFusion(),)

        else:
            raise ValueError(
                f"Unsuppported Retreieval types : {RETRIEVAL_TYPE}"
            )

        # PUBLIC RETRIEVE API

        def retrieve(self,
                    query:str,
                    top_k= TOP_K,
                    )->List[RetrievalResult]:
            logger.info("Retriever started")

            return self.strategy.retrieve(
                query=query,
                top_k=top_k,
            )