from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

load_dotenv()

# Configurações do JWT via .env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Simulação de base de dados
fake_users_db = {
    "jullyen": {
        "username": "jullyen",
        "password": "123456"
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        return None
    return user

def create_access_token(username: str):
    expiration = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": username, "exp": expiration}
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        return {"username": username}
    except JWTError:
        raise credentials_exception
