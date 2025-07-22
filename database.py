# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Para SQLite
DATABASE_URL = "sqlite:///qa_historico.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria as tabelas se não existirem
def init_db():
    Base.metadata.create_all(bind=engine)
