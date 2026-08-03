# CROSS ENCODER BASED RERANKING

from typing import List
from sentence_transformers import CrossEncoder

from core.retrieval_result import RetrievalResult

from reranking.base  import BaseReranker

from config import(
    RERANKER_MODEL,TOP_K
)
from utils.logger import logger

class CrossEncoderReranker(BaseReranker):
    def __init__(self):
        logger.info(f"Loading CrossEncoder : {RERANKER_MODEL}")
        self.model =CrossEncoder(RERANKER_MODEL)

    def rerank(self,
               query : str,
               results : List[RetrievalResult],
               top_k : int = TOP_K,
               ) -> List[RetrievalResult]:
        if not results:
            return []
        pairs = [
            query,result.chunk.text
            for result in results
        ]

        scores= self.model.predict(pairs)
        for result,score in zip(results,scores):
            result.metadata["scores"]["cross_encoder"] =float(score)
            result.score =float(score)
            result.source = "cross_encoder"

        reranked_results = sorted(
            results,
            key = lambda x:x.score,
            reverse =True)        

        for rank,result in enumerate(results,start = 1):

            result.rank = rank

        logger.info(
            f"CrossEncoder{len(reranked_results)} chunks"
        )
        return reranked_results[:top_k]
    