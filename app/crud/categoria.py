from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate

def criar_categoria(db: Session, dados: CategoriaCreate):
    categoria = Categoria(nome=dados.nome)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

def listar_categorias(db: Session):
    return db.query(Categoria).all()

def buscar_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def deletar_categoria(db: Session, categoria: Categoria):
    db.delete(categoria)
    db.commit()