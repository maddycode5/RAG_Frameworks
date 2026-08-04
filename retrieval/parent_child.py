"""
PARENT DOCUMENT RETRIEVAL 
"""

from collections import OrderedDict
from typing import List

from core.chunk import Chunk
from core.retrieval_result import RetrievalResult

from vectordb.chunk_repository import ChunkRepository

from utils.logger import logger

class ParentRetriever:
    def __init__(
            self,
            repository:ChunkRepository,
    ):
        self.repository = repository

    def retrieve(
            self,
            results : List[RetrievalResult],
    ) -> List[Chunk]:
        logger.info("Starting Parent Retrieval")

        parents = OrderedDict()

        for result in results():
            parent_id = result.chunk.metadata.get("parent_id")

            if parent_id is None:
                parents[result.chunk.chunk_id]  = [result.chunk]

                continue

            if parent_id not in parents:
                parents[parent_id] = self.repository.get_by_parent(parent_id)

            merged_chunks = []
            for parent_chunks in parents.values():
                merged_chunks.extend(parent_chunks)

            logger.info(
                f"Parent Retrieval returned {len(merged_chunks)} chunks."
            )

            return merged_chunks
        