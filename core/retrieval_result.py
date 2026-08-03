"""
represents a retrieved chunks along with its retrieval 
meta data and score

used by : 
-Dense Retriever
-Sparse Retriever
-Hybrid Retriever
-Hybrid Retriever
-RRF
-Cross Encoder
"""
from dataclasses import dataclass,field
from typing import Optional,Dict,Any

from core.chunk import Chunk

@dataclass(slots =True)
class RetrievalResult:
    "REpresents a retrieved documents"

    chunk: Chunk
    score:float
    source :str
    rank : Optional[int] = None
    metadata : Dict[str,Any] =field(default_factory =dict)