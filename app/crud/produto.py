from sqlalchemy.orm import Session
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoPrecoUpdate


def criar_produto(db: Session, dados: ProdutoCreate):
    produto = Produto(
        nome=dados.nome,
        preco=dados.preco,
        categoria_id=dados.categoria_id
    )
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto


def listar_produtos(db: Session):
    return db.query(Produto).all()


def buscar_produto(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()


def atualizar_preco_produto(db, produto, novo_preco: float):
    produto.preco = novo_preco
    db.commit()
    db.refresh(produto)
    return produto



def deletar_produto(db: Session, produto: Produto):
    db.delete(produto)
    db.commit()
