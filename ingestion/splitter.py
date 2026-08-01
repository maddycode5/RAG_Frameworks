# recursive Splitter

import uuid
from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import(
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    )

from core.chunk import Chunk
from core.document import Document
from core.base_splitter import BaseSplitter

class RecursiveSplitter(BaseSplitter):
    def __init__(self):
        self.splitter =RecursiveCharacterTextSplitter(
            chunk_size = CHUNK_SIZE,
            chunk_overlap =CHUNK_OVERLAP,
        )

        def split(self,documents : List[Document])-> list[Chunk]:
            chunks = []

            for doc in documents:
                texts = self.splitter.split_text(doc.text)
                for index , text in enumerate(texts):
                    chunks.append(
                        Chunk(
                            chunk_id = uuid.uuid().hex,
                            text=text,
                            metadata = {
                                **doc.metadata,
                                "chunk_index" : index,
                            },
                        )
                    )
                return chunks
             