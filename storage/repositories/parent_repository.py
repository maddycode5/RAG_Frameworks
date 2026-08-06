# store parents chunks 

# - store parent chunks
# retrieve parent chunks
# -save 
# - load


import pickle
from typing import Dict, List
from core.parent_chunk import ParentChunk

from config import VECTOR_STORE_DIR
from utils.logger import logger

class ParentRepository:
    def __init__(self):
        self._parents:Dict[str,ParentChunk] = {}
        self.repository_file = (
            VECTOR_STORE_DIR/
            "parent_chunks.pkl"
        )

    def add(self,
            parents:List[ParentChunk]
            ):
        for parent in parents:
            self._parents[parent.parent_id] = parent

    def get(self,
            parent_id : str):

        return self._parents.get(parent_id)

    def get_many(self,parent_ids : List[str]
                 ):
        return [
            self._parents.get(parent)
            for parent in parent_ids
            if parent in self._parents
        ]

    def save(self):
        with open(self.respository_file,
                  "wb") as file:
            pickle.dump(self._parents,
                        file)

        logger.info(
            f"Saved {len(self._parents)} parent chunks"
        )

    def load(self):
        with open(self.repository_file, "rb")as file:
            self._parents =pickle.load(file)

        logger.info(f"Loaded {len(self._parents)} parent chunks")

    def __len__(self):
        return len(self._parents)

    