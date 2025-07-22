# retriever.py
import faiss
import numpy as np
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

def carregar_chunks(pdf_path="Documento_Mestre_MKT_SolarGroup_FINAL_ORGANIZADO.pdf"):
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() or "" for page in reader.pages])

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(text)
    return chunks

def criar_indice(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    vectors = model.encode(chunks, convert_to_numpy=True)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(np.array(vectors).astype("float32"))
    return index, model, chunks

def buscar_contexto(pergunta: str, index, model, chunks, top_k=2):
    pergunta_vector = model.encode([pergunta]).astype("float32")
    _, indices = index.search(pergunta_vector, top_k)
    trechos = [chunks[i] for i in indices[0]]
    return "\n".join(trechos)
