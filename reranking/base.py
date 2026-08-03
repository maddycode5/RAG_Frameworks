"""
Reranking
- abstract interface for all reranking strategies
"""

from abc import ABC , abstractmethod
from typing import List

from core.retrieval_result import RetrievalResult

class BaseReranker(ABC):
    @abstractmethod
    def rerank(
        self,
        query : str,
        results :List[RetrievalResult],
        top_k : int
    ) -> List[RetrievalResult]:
        """
        Reranked Retrieved documents
        """
        pass
    