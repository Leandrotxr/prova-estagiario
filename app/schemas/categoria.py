from pydantic import BaseModel
from typing import List

class CategoriaBase(BaseModel):
    nome: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaRead(CategoriaBase):
    id: int

    class Config:
        orm_mode = True
