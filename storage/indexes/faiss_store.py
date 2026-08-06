# build and store the faiss vector index

# build faisss Index
# search  vector
# save index
# load index
# maintai index position -> chunk_id mapping

# does not store chunk objects
# /does not perform retrieval fusion
# does not generate embeddings

from pathlib import Path
import pickle
from typing import List

import faiss
import numpy as np 

from core.embeddings import Embedding
from interfaces.base_vectordb import BaseVectorDB

from config import VECTOR_STORE_DIR
from utils.logger import logger

class FAISSStore(BaseVectorDB):
    def __init__(self):
        self.index = None
        self.chunk_ids : List[str] = []
        self.dimension = None
        VECTOR_STORE_DIR.mkdir(parents =True,exist_ok=True)

    # build index

    def build(self,embeddings :List[Embedding]):
        if not embeddings:
            raise ValueError("No embeddings provided")

        vectors = np.array(
            [embedding.vector for embedding in embeddings],
            dtype = np.float32
            )
        self.dimension = vectors.shape[1]
        self.index =faiss.IndexFlatIP(self.dimension)
        self.index.add(vectors)

        self.chunk_ids = [
            embedding.chunk_ids
            for embedding in embeddings
        ]
        logger.info(
            f"Built FAISS index with{len(self.chunk_ids)} vectors."
        )

    def search(self,
               query_vector: np.ndarray,
               top_k: int = 5
               ):

        if self.index is None:
            raise RuntimeError("FAISS index not built")

        query_vector = np.array(
            [query_vector],
            dtype=np.float32
        )

        # perform search on the faiss index
        scores, indices = self.index.search(query_vector, top_k)

        results = []
        for score, index in zip(scores[0], indices[0]):
            if index == -1:
                continue

            results.append((self.chunk_ids[index], float(score)))

        return results

    def save(self):
        if self.index is None:
            raise RuntimeError("Nothing to save")

        faiss.write_index(
            self.index,
            str(VECTOR_STORE_DIR / "faiss.index")
        )

        with open(
            VECTOR_STORE_DIR / "chunk_ids.pkl",
            "wb"
        ) as file:
            pickle.dump(
                self.chunk_ids,
                file
            )

        logger.info("FAISS index saved")

    def load(self):
        self.index = faiss.read_index(
            str(VECTOR_STORE_DIR / "faiss.index")
        )
        with open(
            VECTOR_STORE_DIR / "chunk_ids.pkl",
            "rb"
        ) as file:
            self.chunk_ids = pickle.load(file)

        self.dimension = self.index.d
        logger.info("FAISS index loaded.")


        # count

    def __len__(self):
        if self.index is None:
            return 0
        return self.index.ntotal
        
