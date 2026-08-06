# absract splitter class

from abc import ABC,abstractmethod
from typing import List

from core.document import Document
from core.chunk import Chunk

class BaseSplitter(ABC):
    @abstractmethod
    def split(self,documents:List[Document]) ->List[Chunk]:
        """
        Split documnennts into chunks
        """
        pass

