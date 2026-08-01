# Metadata generator

import datetime
from typing import List

from core.chunk import Chunk

class MetadataGenerator:
    def generate(self , chunks : List[Chunk]) -> List[Chunk]:
        for chunk in chunks:
            chunk.metadata.update(
                {
                    "characters":len(chunk.text),
                    "words" : chunk.word_count,
                    "created_at" : datetime.now().isofformat()
                }
            )
        return chunks
