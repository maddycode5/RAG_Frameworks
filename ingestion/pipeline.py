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
        child_chunks,parent_chunks = self.splitter.split(documents)
        child_chunks = self.metadata_generator.generate(child_chunks)

        return child_chunks,parent_chunks

        