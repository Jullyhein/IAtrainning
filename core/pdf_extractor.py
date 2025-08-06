import fitz
from typing import Tuple


class PDFMetadataExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_text_and_metadata(self) -> Tuple[str, dict]:
        doc = fitz.open(self.pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        metadata = doc.metadata or {}
        metadata["pdf_id"] = self.pdf_path.split("/")[-1]
        return text, metadata
