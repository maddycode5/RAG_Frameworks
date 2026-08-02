from ingestion.pipeline import IngestionPipeline
from embeddings.embedding_pipeline import EmbeddingPipeline
from config import RAW_PDF_DIR

# INGEST DOCUMENTS

ingestion  =IngestionPipeline()
chunks  = ingestion.run(RAW_PDF_DIR)

print(f"Chunks Generated : {len(chunks)}")

# Generate Embeddings
embedding_pipeline = EmbeddingPipeline()
embedded_chunks =embedding_pipeline.run(chunks)

print(f"Embedded Chunks : {len(embedded_chunks)}")

print(type(embedded_chunks[0].embedding))
print(embedded_chunks[0].embedding.shape)
