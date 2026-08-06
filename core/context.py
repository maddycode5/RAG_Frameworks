from dataclasses import dataclass

from typing import List

from core.retrieval_result import RetrievalResult

@dataclass(slots=True)
class Context:
    text :str
    results : List[RetrievalResult]
    total_chars : int
    