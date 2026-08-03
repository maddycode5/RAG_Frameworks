"""
dense retrieval using FAISS

Workflow:
    Query
      ↓
Embedding Model
      ↓
FAISS Search
      ↓
Chunk IDs
      ↓
Chunk Repository
      ↓
Chunk Objects
"""

from typing import List

from core.chunk import Chunk
from core.embeddings import Embedding

from retrieval.base import BaseRetriever

from  embeddings.embedding_model import EmbeddingModel

from vectordb.faiss_store import FAISSStore
from vectordb.chunk_repository import ChunkRepository

from utils.logger import logger

from config import TOP_K

class DenseRetriever(BaseRetriever):
    def __init__(
        self,
        faiss_store :FAISSStore,
        repository : ChunkRepository,
        ):

        self.faiss_store =faiss_store
        self.repository = repository 
        self.embedding_model =EmbeddingModel()

    def retrieve(
        self,
        query : str,
        top_k : int = TOP_K, 
    )-> List[Chunk]:
        logger.info("Dense Retrieval Started")

        # generate query embeddings

        query_vector = self.embedding_model.embed_query(query)

        # SEARCH FAISS

        results = self.faiss_store.search(
            query_vector =query_vector,
            top_k = top_k,)

        # convert ids to chunk objects

        retrieved_chunks = []

        for chunk_id , score in results:
            chunk  =self.repository.get(chunk_id)
            if chunk is None:
                continue
            chunk.score = score

            retrieved_chunks.append(score)

        logger.info(
            f"Dense retriever returend {len(retrieved_chunks)} chunks"
        )

        return retrieved_chunks