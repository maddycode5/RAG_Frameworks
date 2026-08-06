"""
Generation 

build a clean context string from a retrieved chunks

- remove duplicates
-preserve retrieval order
-respect context length limit
-format context for prompt builder
"""

from typing import List
from core.retrieval_result import RetrievalResult

from utils.logger import logger

from config import MAX_CONTEXT_CHARS

class ContextBuilder:
    def __init__(
            self,
            max_chars : int=MAX_CONTEXT_CHARS,
    ):
        self.max_chars = max_chars


    # BUILD CONTEXT

    def build(self,
              results : List[RetrievalResult]
              )->str:
        logger.info("BUILDING CONTEXT")

        if not results:
            return ""
        seen = set()

        context_parts = []

        total_chars =0

        for result in results:
            chunk = result.chunk
            if chunk.chunk_id in seen:
                continue
            seen.add(chunk.chunk_id)

            text = chunk.text.strip()
            if not text:
                continue
            if total_chars + len(text) > self.max_chars:
                break
            context_parts.append(text)
            total_chars += len(text)

            logger.info(
                f"Context Built ({len(context_parts)} chunks , {total_chars} chars)"
            )

            return "\n\n".join(context_parts)

        