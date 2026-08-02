from dataclasses import dataclass
import numpy as np

@dataclass
class Embedding:
    chunk_id :str
    vector : np.ndarray

    