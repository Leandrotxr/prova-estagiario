from fastapi import FastAPI

from app.router import produto, categoria
from app.db.base import Base
from app.db.sessao import engine

app = FastAPI(title="API de Produtos")

Base.metadata.create_all(bind=engine)

app.include_router(produto.router)
app.include_router(categoria.router)
