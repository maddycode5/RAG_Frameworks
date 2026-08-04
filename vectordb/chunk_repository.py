# stores the chnks using chunk_id

# store chunks 
# retreive one chunk
# retrieve multiple chunks 

from typing import Dict , List
from core.chunk import Chunk
import pickle
from utils.logger import logger

from config import VECTOR_STORE_DIR

class ChunkRepository:
    def __init__(self):
        self._chunks :Dict[str, Chunk] = {}
        self._parent_index :Dict[str,List[str]] = {}
        self.repository_file = VECTOR_STORE_DIR/"chunks.pkl"

    def add(self,chunks : List[Chunk]):
        for chunk in chunks:
            self._chunks[chunk.chunk_id]=chunk
            parent_id = chunk.metadata.get("parent_id")

            if parent_id:
                self._parent_index.setdefault(
                    parent_id,
                    []
                ).append(chunk.chunk_id)

    def get(self,chunk_id : str)->Chunk:
        return self._chunks.get(chunk_id)

    def get_many(self,chunk_ids: List[str])  -> List[Chunk]:
        return  [
            self._chunks[cid]
            for cid in chunk_ids
            if cid in self._chunks
        ] 

    def __len__(self):
        return len(self._chunks)

    def save(self):
        with open(self.repository_file, "wb") as file:
            pickle.dump(self._chunks,file)

        logger.info(f"Saved {len(self._chunks)} chunks.")

    def load(self):
        with open(self.repository_file,"rb") as file:
            self._chunks = pickle.load(file)

        self._parent_index = {}
        for chunk in self._chunks.values():
            parent = chunk.metadata.get("parent_id")
            if parent:
               self._parent_index.setdefault(parent,[]).append(chunk.chunk_id)

                    
        logger.info(f"Loaded {len(self._chunks)} chunks")

    def get_by_parent(self,parent_id:str):
        
        chunk_ids =self._parent_index.get(
            parent_id,
            [])

        return [
            self._chunks[cid]

            for cid in chunk_ids
        ]

    def exists(self,
               chunk_id : str
               )->bool:

        return chunk_id in self._chunks

        