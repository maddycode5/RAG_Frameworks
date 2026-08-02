from ingestion.pipeline import IngestionPipeline
from embeddings.embedding_pipeline import EmbeddingPipeline
from vectordb.manager import IndexManager

from config import RAW_PDF_DIR

# ingestion
ingestion =IngestionPipeline()
chunks =  ingestion.run(RAW_PDF_DIR)

# embeddings
embedding_pipline = EmbeddingPipeline()
embeddings = embedding_pipline.run(chunks)

# index manager

manager = IndexManager()
manager.build(chunks,embeddings)
manager.save()

print("Hybrid Index Built sucessfully")

