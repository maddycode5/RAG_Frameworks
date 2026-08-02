"""
VECTOR DATABASE

central manager for all indexing components
- build all indexes
- save them
- load them 
-expose repository and vector stores

does not perform retrieval
does not generate embeddings
"""
from typing import List

from core.chunk import Chunk
from core.embeddings import Embedding

from vectordb.chunk_repository import ChunkRepository
from vectordb.faiss_store import FAISSStore
from vectordb.bm25_store import BM25Store

from utils.logger import logger

class IndexManager:
    def __init__(self):
        self.repository =ChunkRepository()
        self.faiss_store =FAISSStore()
        self.bm25_store=BM25Store()

        # build indexes

    def build(
            self,
            chunks : List[Chunk],
            embeddings :List[Embedding]
        ):

        logger.info("Building Index Manager..")

        # store chunk objects
        self.repository.add(chunks)

        # build dense index
        self.faiss_store.build(embeddings)

        # build sparse index
        self.bm25_store.build(chunks)

        logger.info("Index manager build completed")


    # save indexes

    def save(self):
        logger.info("Saving Indexes..")
        self.faiss_store.save()
        self.bm25_store.save()
        logger.info("Indexes saved successfully")

    # load indexes
    def load(self):
        logger.info("Loading Indexes")

        self.faiss_store.load()
        self.bm25_store.load()

        logger.info("Indexes loaded sucessfully")

    def get_repository(self):
        return self.repository

    def get_faiss_store(self):
        return self.faiss_store

    def get_bm25_store(self):
        return self.bm25_store

    
