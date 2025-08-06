from fastapi import FastAPI
from api.endpoints import router
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import router

app = FastAPI(title="IA Solar Group - Perguntas e Respostas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
