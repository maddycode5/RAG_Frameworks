# publicreranking interface

from typing import List
from config import (
    USE_RERANKER,
    TOP_K,
)

from core.retrieval_result import RetrievalResult
from reranking.cross_encoder import CrossEncoderReranker

from utils.logger import logger

class Reranker:
    def __init__(self):
        if USE_RERANKER:
            logger.info("CrossEncoder Enabled")
            self.strategy =CrossEncoderReranker()

        else:
            logger.info("ReRanker Disabled")
            self.strategy =None

    def rerank(self,
               query:str,
               results :List[RetrievalResult],
               top_k:int=TOP_K,
               )->List[RetrievalResult]:

        if self.strategy is None:
            return results[:top_k]
        return self.strategy.rerank(
            query=query,
            results =results,
            top_k =top_k,
        )