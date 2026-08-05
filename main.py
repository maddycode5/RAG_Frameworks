from ingestion.pipeline import IngestionPipeline
from embeddings.embedding_pipeline import EmbeddingPipeline
from vectordb.index_manager import IndexManager

from config import RAW_PDF_DIR

# ingestion
ingestion =IngestionPipeline()
child_chunks,parent_chunks =  ingestion.run(RAW_PDF_DIR)

# embeddings
embedding_pipline = EmbeddingPipeline()
embeddings = embedding_pipline.run(child_chunks)

# index manager

manager = IndexManager()
manager.build(child_chunks =child_chunks,
            parent_chunks=parent_chunks,
            embeddings = embeddings)

manager.save()

print("Indexing Completed sucessfully")

