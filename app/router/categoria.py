from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.router.deps import get_db
from app.crud import categoria
from app.schemas.categoria import CategoriaCreate, CategoriaRead

router = APIRouter(prefix="/categorias")

@router.get("/")
def listar_categorias(db: Session = Depends(get_db)):
    return categoria.listar_categorias(db)

@router.post("/criar_categoria")
def criar_categoria(dados: CategoriaCreate, db: Session = Depends(get_db)):
    return categoria.criar_categoria(db, dados)

@router.get("/{categoria_id}")
def buscar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria_buscada = categoria.buscar_categoria(db, categoria_id)

    if categoria_buscada is None:
        raise HTTPException(404, "Categoria não encontrada")

    return categoria_buscada

@router.delete("/{categoria_id}")
def deletar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria_buscada = categoria.buscar_categoria(db, categoria_id)

    if categoria_buscada is None:
        raise HTTPException(404, "Categoria não encontrada")

    categoria.deletar_categoria(db, categoria_buscada)
    return {"msg": "Categoria deletada"}