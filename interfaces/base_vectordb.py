# absract vector database class

from abc import ABC,abstractmethod

class VectorDB(ABC):
    @abstractmethod

    def add(self,embeddings,metadata):
        pass

    @abstractmethod
    def search(self,query_embedding,top_k):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass

    