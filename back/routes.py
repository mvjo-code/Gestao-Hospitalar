from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import session_local

router = APIRouter() # instância do roteador para organizar as rotas

def get_db():
    db = session_local() # cria uma sessão de banco de dados
    try:
        yield db # retorna a sessão para uso nas rotas
    finally:
        db.close() # garante que a sessão seja fechada após o uso



