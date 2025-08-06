from core.pdf_extractor import PDFMetadataExtractor
from core.pdf_splitter import PDFTextSplitter
from core.embedding_store import EmbeddingStore
from core.qa_system import QASystem

# Carrega tudo uma vez só ao iniciar a API
pdf_path = "./Documento_Mestre_MKT_SolarGroup_FINAL_ORGANIZADO.pdf"

extractor = PDFMetadataExtractor(pdf_path)
text, metadata = extractor.extract_text_and_metadata()

splitter = PDFTextSplitter()
documents = splitter.split(text, metadata)

embedder = EmbeddingStore()
vectorstore = embedder.build_vectorstore(documents)

qa_system_instance = QASystem(vectorstore, metadata)
