from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.router.deps import get_db
from app.crud import produto, categoria
from app.schemas.produto import ProdutoCreate, ProdutoPrecoUpdate, ProdutoDelete, ProdutoRead

router = APIRouter(prefix="/produtos")

@router.get("/", response_model=list[ProdutoRead])
def listar_produtos(db: Session = Depends(get_db)):
    return produto.listar_produtos(db)

@router.post("/criar_produto", response_model=ProdutoRead, status_code=201)
def criar_produto(dados: ProdutoCreate, db: Session = Depends(get_db)):
    if dados.preco < 0:
        raise HTTPException(status_code=400, detail="Não é possível colocar um preço menor que 0")

    categoria_buscada = categoria.buscar_categoria(db, dados.categoria_id)
    if categoria_buscada is None:
        raise HTTPException(404, "Categoria não encontrada")

    return produto.criar_produto(db, dados)

@router.get("/{produto_id}", response_model=ProdutoRead)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto_buscado = produto.buscar_produto(db, produto_id)

    if produto_buscado is None:
        raise HTTPException(404, "Produto não encontrado")

    return produto_buscado

@router.patch("/atualizar_preco", response_model=ProdutoRead)
def atualizar_preco(dados: ProdutoPrecoUpdate, db: Session = Depends(get_db)):

    if dados.preco < 0:
        raise HTTPException(status_code=400, detail="Não é possível colocar um preço menor que 0")

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

