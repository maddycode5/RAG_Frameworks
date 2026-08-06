"""
Vector_database

build and manage the BM25 keyword index
- tokenise the chunks 
-build bm25 inddex
-search keywords
-save index 
- load index

-does not store vectors
-does not generate the vectors
- does not store chunk objects  
"""

from pathlib import Path
from typing import List
import pickle

from rank_bm25 import BM25Okapi
from core.chunk import Chunk
from utils.logger import logger
from config import VECTOR_STORE_DIR

class BM25Store:
    def __init__(self):
        self.bm25=None
        self.corpus =[]
        self.chunk_ids = []

        VECTOR_STORE_DIR.mkdir(parents =True,exists_ok=True)

    def tokenizer(self,text:str):
        return text.lower().split()

    def build(self,chunks : List[Chunk]):
        if not chunks:
            raise ValueError("NO chunks Provided")
        
        self.corpus = [
            self.tokenizer(chunk.text)
            for chunk in chunks
        ]

        self.chunk_ids = [
            chunk.chunk_id
            for chunk in chunks
        ]

        self.bm25 =BM25Okapi(self.corpus)
        logger.info(
            f"Built BM25 index with {len(chunks)} chunks"
        )

    def search(self,
            query:str,
            top_k : int=  5
           ):
            
        if self.bm25 is None:
            raise RuntimeError("BM25 index  not built")
        
        query_tokens = self.tokenize(query)
        scores =self.bm25.get_scores(query_tokens)
        ranked =sorted(
            zip(self.chunk_ids,scores),
            key=lambda x:x[1],
            reverse=True
        )
        return ranked[:top_k]

    def save(self):
        with open(VECTOR_STORE_DIR / "bm25.pkl",
                  "wb"
                  ) as file:
            pickle.dump(
                {"bm25" : self.bm25,
                "chunk_ids" : self.chunk_ids,
                "corpus" : self.corpus,
                },
                file,
            )
        logger.info("BM25 index saved")


    def load(self):
        with open(VECTOR_STORE_DIR /"bm25.pkl",
                "rb"
                ) as file:
            data =pickle.load(file)
        self.bm25 = data["bm25"]
        self.chunk_ids =data["chunk_ids"]
        self.corpus = data["corpus"]
        logger.info("BM25 index loaded")

    def __len__(self):
        return len(self.chunk_ids)


