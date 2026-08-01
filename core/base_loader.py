
# ABSRACT CLASS FOR LOADING DOCUMENTS FROM A SOURCE

from abc import ABC,abstractmethod
from typing import List

from core.document import Document


class BaseLoder(ABC):
    @abstractmethod
    def load(self) -> List[Document]:
        """
        Load Documnets from a source
        """
        pass   

