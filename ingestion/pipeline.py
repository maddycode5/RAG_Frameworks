# INGESTION PIPELINE

from ingestion.loader import PDFLoader
from ingestion.splitter import RecursiveSplitter
from ingestion.metadata import MetadataGenerator

class IngestionPipeline:
    def __init__(self):
        self.loader =PDFLoader()
        self.splitter = RecursiveSplitter()
        self.metadata_generator  = MetadataGenerator()

    def run(self,folder_path):
        documents = self.loader.load(folder_path)
        chunks = self.splitter.split(documents)
        chunks =self.metadata.generate(chunks)

        return chunks

        