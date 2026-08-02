# EMBEDDING PIPELINE


from core.chunk import Chunk

from embeddings.embedding_model import EmbeddingModel
from embeddings.cache import EmbeddingCache

from utils.logger import logger

class EmbeddingPipeline:

    def __init__(self):
        self.model = EmbeddingModel()

        self.cache = EmbeddingCache()

    def run(self,chunks : list[Chunk]) -> list[Chunk]:
        logger.info("Starting Embedding Pipeline")\

        texts =[]
        chunk_indices= []

        for idx,chunk in enumerate(chunks):

            if self.cache.exists(chunk.texts):
                chunk.embedding =self.cache_load(chunk.text)

            else:
                texts.append(chunk.text)
                chunk_indices.append(idx)

        if texts:
            embeddings = self.model.embed(texts)
            for idx, embedding in zip(chunk_indices , embeddings):
                chunk[idx].embedding = embedding
                self.cache.save(chunk[idx].text,embedding)

        logger.info(f"Embedd {len(chunks)} chunks")

        return chunks

    