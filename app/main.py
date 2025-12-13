from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import produto, categoria
from app.db.base import Base
from app.db.sessao import engine

app = FastAPI(title="API de Produtos")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

Base.metadata.create_all(bind=engine)

app.include_router(produto.router)
app.include_router(categoria.router)
