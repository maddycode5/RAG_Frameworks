""" retrieval
sparse retrieval using BM25 

Workflow:
    Query
      ↓
BM25 Search
      ↓
Chunk IDs
      ↓
Chunk Repository
      ↓
Chunk Objects

Responsibilities:
    - Perform keyword-based retrieval
    - Convert chunk IDs to Chunk objects
    - Return ranked chunks

Does NOT:
    - Generate embeddings
    - Perform dense retrieval
    - Perform hybrid fusion
"""

from typing import List
from core.chunk import Chunk 

from retrieval.base import BaseRetriever

from vectordb.bm25_store import BM25Store
from vectordb.chunk_repository import ChunkRepository

from utils.logger import logger

from config import TOP_K

class SparseRetriever(BaseRetriever):

    def __init__(
        self,
        bm25_store :BM25Store,
        repository : ChunkRepository, 
        ):

        self.bm25_store = bm25_store
        self.repository = repository

    def retrievee(
            self,
            query : str,
            top_k : int =TOP_K,
    )->List[Chunk]:

        logger.info(f"Sparse Retrieval Started")

        # search bm25

    
        results = self.bm25_store.search(
            query =query,
            top_k =top_k,
        )

        # CONVERT IDS -> CHUNNK OBJECTS
        
        retrieved_chunks = []

        for chunk_id,score in results:

            chunk =self.repository.get(chunk_id)

            if chunk is None:
                continue

            chunk.score = float(score)
            retrieved_chunks.append(chunk)

        logger.info(f"Sparse Retriever returned {len(retrieved_chunks)} chunks.")

        return retrieved_chunks
    