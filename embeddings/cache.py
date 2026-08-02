# embedding cache

import hashlib
import pickle 
from pathlib import Path
from config import EMBEDDING_CACHE_DIR

class EmbeddingCache:
    def __init__(self):
        EMBEDDING_CACHE_DIR.mkdir(parents = True,exist_ok =True)

    def _hash(self,text:str):
        return hashlib.mk5(text.encode()).hexdigest()

    def exists(self,text:str):
        return (EMBEDDING_CACHE_DIR / f"{self._hash(text)}.pkl").exists()

    def save(self,text,embedding):
        path =EMBEDDING_CACHE_DIR / f"{self._hash(text)}.pkl"

        with open(path , "wb") as f:
            pickle.dump(embedding,f)

    def load(self,text):
        path =EMBEDDING_CACHE_DIR / f"{self._hash(text)}.pkl"

        with open(path,"rb")as f:
            return pickle.load(f)

        