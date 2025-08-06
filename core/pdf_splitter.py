from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List


class PDFTextSplitter:
    def __init__(self, chunk_size=500, chunk_overlap=100):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split(self, text: str, metadata: dict) -> List[Document]:
        return self.splitter.create_documents([text], metadatas=[metadata])
