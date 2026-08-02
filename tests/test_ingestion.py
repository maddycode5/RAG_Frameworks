from ingestion.pipeline import IngestionPipeline
from config import RAW_PDF_DIR

pipeline =IngestionPipeline()
chunks = pipeline.run(RAW_PDF_DIR)
print(f"Chunks generated: {len(chunks)}" )

for chunk in chunks[:3]:
    print(chunk.metadata)
    print(chunk.preview())
    print("_" * 80)

    
