from pydantic import BaseModel
from app.schemas.categoria import CategoriaRead


class ProdutoBase(BaseModel):
    nome: str
    preco: float


class ProdutoCreate(ProdutoBase):
    categoria_id: int


class ProdutoRead(ProdutoBase):
    id: int
    categoria: CategoriaRead

    class Config:
        from_attributes = True


class ProdutoPrecoUpdate(BaseModel):
    id: int
    preco: float


class ProdutoDelete(BaseModel):
    id: int
