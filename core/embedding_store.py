from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List, Optional

class EmbeddingStore:
    """
    Classe para construir um vectorstore Chroma a partir de documentos usando HuggingFace embeddings.
    """
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Inicializa o embedder com o modelo HuggingFace especificado.
        
        :param model_name: Nome do modelo de embeddings da HuggingFace.
        """
        self.embedder = HuggingFaceEmbeddings(model_name=model_name)

    def build_vectorstore(
        self,
        docs: List[Document],
        persist_directory: Optional[str] = None
    ) -> Chroma:
        """
        Cria um Chroma vectorstore a partir de uma lista de documentos.
        
        :param docs: Lista de objetos `Document` para indexação.
        :param persist_directory: Diretório opcional para persistir o banco Chroma.
        :return: Instância do vectorstore Chroma.
        """
        return Chroma.from_documents(
            documents=docs,
            embedding=self.embedder,
            persist_directory=persist_directory
        )
