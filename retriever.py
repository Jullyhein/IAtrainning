# retriever.py
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pypdf import PdfReader
import os

CHROMA_DIR = "chroma_db"  # Caminho do banco vetorial persistente
PDF_PATH = "Documento_Mestre_MKT_SolarGroup_FINAL_ORGANIZADO.pdf"
EMBEDDING_MODEL_NAME = "gpt-4o-mini"

def carregar_chunks(pdf_path=PDF_PATH):
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() or "" for page in reader.pages])
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    chunks = splitter.split_text(text)
    return chunks

def criar_banco_vetorial(chunks):
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )
    db.persist()
    return db

def carregar_banco_vetorial():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    if not os.path.exists(CHROMA_DIR) or not os.listdir(CHROMA_DIR):
        chunks = carregar_chunks()
        return criar_banco_vetorial(chunks)
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)

def buscar_contexto(pergunta: str, top_k=3):
    db = carregar_banco_vetorial()
    resultados = db.similarity_search(pergunta, k=top_k)
    return "\n\n".join([r.page_content for r in resultados])
