# models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class QA(Base):
    __tablename__ = "qa_pairs"

    id = Column(Integer, primary_key=True)
    pergunta = Column(Text, nullable=False)
    resposta = Column(Text, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)
