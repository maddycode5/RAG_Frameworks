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
from core.parent_chunk import ParentChunk
from core.embeddings import Embedding

from vectordb.chunk_repository import ChunkRepository
from vectordb.parent_repository import ParentRepository
from vectordb.faiss_store import FAISSStore
from vectordb.bm25_store import BM25Store

from utils.logger import logger

class IndexManager:
    def __init__(self):
        self.chunk_repository =ChunkRepository()
        self.parent_repository = ParentRepository()
        self.faiss_store =FAISSStore()
        self.bm25_store=BM25Store()

        # build indexes

    def build(
            self,
            child_chunks : List[Chunk],
            parent_chunks : List[ParentChunk],
            embeddings :List[Embedding],
            
        ):

        logger.info("Building Index Manager..")

        # store child chunk 
        self.chunk_repository.add(child_chunks)

        # store parent chunks
        self.parent_repository.add(parent_chunks)

        # build dense index
        self.faiss_store.build(embeddings)

        # build sparse index
        self.bm25_store.build(child_chunks)

        logger.info("Index manager build completed")


    # save indexes

    def save(self):
        logger.info("Saving Indexes..")
        self.chunk_repository.save()
        self.parent_repository.save()
        self.faiss_store.save()
        self.bm25_store.save()
        logger.info("Indexes saved successfully")

    # load indexes
    def load(self):
        logger.info("Loading Indexes")
        
        self.chunk_repository.load()
        self.parent_repository.load()
        self.faiss_store.load()
        self.bm25_store.load()

        logger.info("Indexes loaded sucessfully")

    def get_chunk_repository(self):
        return self.chunk_repository

    def get_parent_repository(self):
        return self.parent_repository

    def get_faiss_store(self):
        return self.faiss_store

    def get_bm25_store(self):
        return self.bm25_store

    
