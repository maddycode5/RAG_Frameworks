"""
represents a parent documnet chunk

USED BY:
- parent retriever
- parent repository 
"""

from dataclasses import dataclass,field
from typing import Dict,Any

@dataclass(slots =True)
class ParentChunk:

    """
    Represents the Parent chunk from which 
    multiplechild chunks are generated 
    """
    parent_id : str
    text : str
    metadata : Dict[str, Any] =field(deafult_factory = dict)

    def __len__(self):
        return len(self.text)

    @property
    def word_count(self):
        return len(self.text.split())

    def preview(self,chars : int = 80):
        return self.text[:chars] + (
            "..."
            if len(self.text) >chars
            else ""
        )

    def to_dict(self):
        return {
            "parent_id" : self.parent_id,
            "text" : self.text,
            "metadata" : self.metadata
        }

    
