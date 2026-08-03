# retrieval

# abstract interface for all retrieval strategies
# define a common retreival api

from abc import ABC,abstractmethod
from typing import List

from core.chunk import Chunk

class BaseRetriever(ABC):
    @abstractmethod
    def retrievee(
        self,
        query:str,
        top_k = 5
        ) -> List[Chunk]:
        # Retrieve relevant chunks

        pass

    

