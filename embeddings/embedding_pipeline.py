# EMBEDDING PIPELINE

from typing import List
from core.chunk import Chunk
from core.embeddings import Embedding

from embeddings.embedding_model import EmbeddingModel
from embeddings.cache import EmbeddingCache

from utils.logger import logger

class EmbeddingPipeline:

    def __init__(self):
        self.model = EmbeddingModel()

        self.cache = EmbeddingCache()

    def run(self,chunks : List[Chunk]) -> List[Embedding]:
        logger.info("Starting Embedding Pipeline")

        texts =[]
        chunk_indices= []
        embedding_objects = []

        for idx,chunk in enumerate(chunks):

            if self.cache.exists(chunk.text):
                cached_vector = self.cache.load(chunk.text)

                embedding_objects.append(
                    Embedding(
                        chunk_id = chunk.chunk_id,
                        vector = cached_vector
                    )
                )

            else:
                texts.append(chunk.text)
                chunk_indices.append(idx)

        if texts:
            vectors = self.model.embed(texts)
            for idx, vector in zip(chunk_indices , vectors):
                self.cache.save(chunks[idx].text,vector)
                embedding_objects.append(
                    Embedding(
                        chunk_id = chunks[idx].chunk_id,
                        vector = vector
                    )
                )
                

        logger.info(f"Successfully generated embeddings for {len(embedding_objects)} chunks")

        return embedding_objects

    