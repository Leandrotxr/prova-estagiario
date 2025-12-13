from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.router.deps import get_db
from app.crud import produto
from app.schemas.produto import ProdutoCreate, ProdutoPrecoUpdate, ProdutoDelete

router = APIRouter(prefix="/produtos")

@router.get("/")
def listar_produtos(db: Session = Depends(get_db)):
    return produto.listar_produtos(db)

@router.post("/criar_produto")
def criar_produto(dados: ProdutoCreate, db: Session = Depends(get_db)):
    return produto.criar_produto(db, dados)

@router.get("/{produto_id}")
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto_buscado = produto.buscar_produto(db, produto_id)

    if produto_buscado is None:
        raise HTTPException(404, "Produto não encontrado")

    return produto_buscado

@router.patch("/atualizar_preco")
def atualizar_preco(dados: ProdutoPrecoUpdate, db: Session = Depends(get_db)):
    produto_buscado = produto.buscar_produto(db, dados.id)

    if produto_buscado is None:
        raise HTTPException(404, "Produto não encontrado")

    return produto.atualizar_preco_produto(db, produto_buscado, dados.preco)


@router.delete("/deletar_produto")
def deletar_produto(dados: ProdutoDelete, db: Session = Depends(get_db)):
    produto_buscado = produto.buscar_produto(db, dados.id)

    if produto_buscado is None:
        raise HTTPException(404, "Produto não encontrado")

    produto.deletar_produto(db, produto_buscado)
    return {"msg": "Produto removido com sucesso"}

