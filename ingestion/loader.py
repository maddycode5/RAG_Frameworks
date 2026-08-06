# load documents and convert them into document objects

from pathlib import Path
from typing import List

import fitz

from interfaces.base_loader import BaseLoader
from core.document import Document
from utils.logger import logger
from utils.helpers import clean_text
from core.exceptions import DocumentLoadError

class PDFLoader(BaseLoader):
    def load(self,folder_path:str) -> List[Document]:
        documents = []
        folder = Path(folder_path)
        if not folder.exists():
            raise FileNotFoundError(f"{folder} does not exist.")   
        pdf_files = sorted(folder.glob("*.pdf"))

        if not pdf_files:
            logger.warning("No PDF files found")
            return []

        for pdf in pdf_files:
            try:
                pdf_docs = fitz.open(pdf)
                for page_number ,page in enumerate(pdf_docs):
                    text = clean_text(page.get_text())
                    if not text.strip():
                        continue
                    documents.append(
                        Document(
                            text=text,
                            metadata={
                                "source" : pdf.name,
                                "page" : page_number + 1,
                            },    
                        )
                    )
                pdf_docs.close()
                logger.info(f"Loaded {pdf.name}")

            except Exception as e:
                raise DocumentLoadError(f"Failed to load {pdf.name}: {str(e)}")
        logger.info(f"Loaded{len(documents)} pages.")
        return documents

     