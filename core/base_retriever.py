#abstract retreiver ineterface

from abc import ABC,abstractmethod
from typing import List

from core.chunk import Chunk

class BaseRetriever(ABC):
    @abstractmethod

    def retrieve(self,query:str) -> List[Chunk]:
        """
        Retriever Relevant chunk
        """
        pass