from dataclasses import dataclass , field
from typing import Dict,Any,Optional

@dataclass 
class Chunk:
    """Represent a chunk generated from a document"""

    chunk_id : str
    text:str
    metadata : Dict[str,Any] = field(default_factory = dict)

    embeddings :Optional[list] =None

    def __len__(self) ->int:
        """Number of characters"""

        return len(self.text)

    @property

    def word_count(self) -> int:
        """number of words"""
        return len(self.text.split())

    def preview(self,chars:int = 80):
        """preview first few characters"""
        return self.text[:chars] + ("..."if len(self.text)>chars else"")

    def to_dict(self):
        return {
            "chunk_id" :self.chunk_id,
            "text" : self.text,
            "metadata" : self.metadata,
            "embedding" : self.embedding
        }

    