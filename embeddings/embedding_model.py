# loads and manages  the embedding model

# input :
    # List[str]

# output : 
    # np.ndarray

from sentence_transformers import SentenceTransformer
import numpy as np

from config import (
    EMBEDDING_MODEL,
    EMBEDDING_DEVICE,
    NORMALIZE_EMBEDDINGS
)

from utils.logger import logger

class EmbeddingModel:
    def __init__(self):
        logger.info(f"Loading Embedding Model : {EMBEDDING_MODEL}")

        self.model = SentenceTransformer(
            EMBEDDING_MODEL,
            device = EMBEDDING_DEVICE
        )

        logger.info("Embedding Model Loaded Successfully")

    def embed(self,texts:list[str]) -> np.ndarray:
        embeddings =-self.model.encode(
            texts,convert_to_numpy=True,
            nomalize_embeddings =NORMALIZE_EMBEDDINGS,
            show_progress_bar=True
        )

        return embeddings
    def embed_query(self,query : str) -> np.ndarray:
        embedding =self.model.encode(
            query,
            convert_to_numpy =True,
            normalize_embeddings =NORMALIZE_EMBEDDINGS
        )

        return embedding
    