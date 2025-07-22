# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from retriever import carregar_chunks, criar_indice, buscar_contexto
from llm import gerar_resposta
from database import SessionLocal, init_db
from models import QA

model_name = "declare-lab/flan-alpaca-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
device = torch.device("cpu")
model.to(device)

# Inicializa FastAPI
app = FastAPI(title="API IA Solar Group")

# Libera CORS (opcional, útil para testes com frontend/Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa banco e vetoriza PDF
init_db()
chunks = carregar_chunks()
index, embedder, all_chunks = criar_indice(chunks)

# Schema para entrada da API
class PerguntaEntrada(BaseModel):
    pergunta: str

@app.post("/responder")
def responder(entrada: PerguntaEntrada):
    pergunta = entrada.pergunta.strip()

    # Busca o contexto relevante no PDF
    contexto = buscar_contexto(pergunta, index, embedder, all_chunks)

    # Gera resposta com LLM
    resposta = gerar_resposta(pergunta, contexto).strip()
    import time
    start = time.time()
    # gerar resposta aqui
    print("Tempo total:", time.time() - start)

    # Registra no banco
    db = SessionLocal()
    novo_qa = QA(pergunta=pergunta, resposta=resposta)
    db.add(novo_qa)
    db.commit()
    db.refresh(novo_qa)
    db.close()

    return {
        "pergunta": pergunta,
        "resposta": resposta
    }
