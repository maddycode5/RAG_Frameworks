"""
Generation 

defines the abstract interface of all LLM Generators

- define commmon api for text generation
- ensure all generators expose the same methods

-OllamaGnerator
-OpenAI Generator
-GeminiGenerator
-ClaudeGenerator

"""

from abc import ABC, abstractmethod
from typing import Optional,List

from core.retrieval_result import RetrievalResult

class BaseGenerator(ABC):
    """Abstract base class for all LLM generators"""

    @abstractmethod
    def generate(
        self,
        query:str,
        context : List[RetrievalResult],
        system_prompt : Optional[str] =None,
    ) -> str:
        """Generate an answer from the given query and retrieved context
        Parameters 

        query : str
            -User's question
        
        context : List[RetrievalResult]
                -retrieved and reranked context

        returns 
            str
                - Generated answer
        """

        pass

    @abstractmethod
    def stream(self,
               query:str,
               context :List[RetrievalResult],
               ):
        """
        Stream the generated response.

        Returns

        Iterate[str]
            streamed response tokens
        """
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """
        Check whether the underlying LLM service is available.
        
        returns
            Bool
        """
        pass