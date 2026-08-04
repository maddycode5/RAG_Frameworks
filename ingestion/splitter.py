# recursive Splitter

import uuid
from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import(
    PARENT_CHUNK_SIZE,
    PARENT_CHUNK_OVERLAP,
    CHILD_CHUNK_OVERLAP,
    CHILD_CHUNK_SIZE,
    )

from core.chunk import Chunk
from core.document import Document
from core.base_splitter import BaseSplitter

class RecursiveSplitter(BaseSplitter):
    def __init__(self):
        self.parent_splitter =RecursiveCharacterTextSplitter(
            chunk_size = PARENT_CHUNK_SIZE,
            chunk_overlap = PARENT_CHUNK_OVERLAP,
        )

        self.child_splitter =RecursiveCharacterTextSplitter(
            chunk_size = CHILD_CHUNK_SIZE,
            chunk_overlap = CHILD_CHUNK_OVERLAP,
        )



        def split(self,documents : List[Document])-> list[Chunk]:
            chunks = []
    
            for doc in documents:

                parent_chunks =self.parent_splitter.split_text(doc.text)

                for parent_index , parent_text in enumerate(parent_chunks):
                    parent_id = uuid.uuid4().hex

                    child_chunks = self.child_splitter.split_text(parent_text)

                    for child_index,child_text in enumerate(child_chunks):
                        chunks.append(
                            Chunk(
                                chunk_id =uuid.uuid4().hex,
                                text = child_text,
                                metadata = {
                                    **doc.metadata,
                                    "parent_id" : parent_id,
                                    "parent_index" : parent_index,
                                    "child_index"  :child_index,
                                }
                            )
                        )

                        
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
            