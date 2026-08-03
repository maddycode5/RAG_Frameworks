# stores the chnks using chunk_id

# store chunks 
# retreive one chunk
# retrieve multiple chunks 

from typing import Dict , List
from core.chunk import Chunk
import pickle
from utils.logger import logger
class ChunkRepository:
    def __init__(self):
        self._chunks :Dict[str, Chunk] = {}

    def add(self,chunks : List[Chunk]):
        for chunk in chunks:
            self._chunks[chunk.chunk_id]=chunk

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

        logger.info(f"Saved {len(self.chunks)} chunks.")

    def load(self):
        with open(ChunkRepository,"rb") as file:
            self._chunks = pickle.load(file)

        logger.info(f"Loaded {len(self._chunks)} chunks")