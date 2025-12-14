from app.crud import produto as crud_produto
from app.schemas.produto import ProdutoCreate
from app.models.produto import Produto
from app.models.categoria import Categoria

def test_criar_produto(db):
    categoria = Categoria(nome="Eletrônicos")
    db.add(categoria)
    db.commit()
    db.refresh(categoria)

    dados = ProdutoCreate(nome="Notebook", preco=3500.00, categoria_id = categoria.id)

    prod = crud_produto.criar_produto(db, dados)

    assert prod.id is not None
    assert prod.nome == "Notebook"
    assert prod.preco == 3500.00
    assert prod.categoria_id == categoria.id


def test_listar_produtos(db):
    categoria = Categoria(nome="Eletrônicos")
    db.add(categoria)
    db.commit()
    db.refresh(categoria)

    crud_produto.criar_produto(db, ProdutoCreate(nome="Notebook", preco=3500.00, categoria_id=categoria.id))
    crud_produto.criar_produto(db, ProdutoCreate(nome="Celular", preco=5000.00, categoria_id=categoria.id))

    produtos = crud_produto.listar_produtos(db)
    assert len(produtos) == 2
    assert produtos[0].categoria is not None

def test_buscar_produto_por_id(db):
    categoria = Categoria(nome="Eletrônicos")
    db.add(categoria)
    db.commit()
    db.refresh(categoria)

    produto = crud_produto.criar_produto(db, ProdutoCreate(nome="Notebook", preco=3500.00, categoria_id=categoria.id))

    produto_buscado = crud_produto.buscar_produto(db, produto.id)

    assert produto_buscado is not None
    assert produto_buscado.id == produto.id
    assert produto_buscado.categoria.nome == "Eletrônicos"

def test_buscar_produto_inexistente(db):
    produto = crud_produto.buscar_produto(db, 999)
    assert produto is None

def test_atualizar_preco_produto(db):
    categoria = Categoria(nome="Eletrônicos")
    db.add(categoria)
    db.commit()
    db.refresh(categoria)

    produto = crud_produto.criar_produto(db, ProdutoCreate(nome="Notebook", preco=3500.00, categoria_id=categoria.id))

    produto_atualizado = crud_produto.atualizar_preco_produto(db, produto,5000.00)

    assert produto_atualizado.preco == 5000.00

def test_deletar_produto(db):
    categoria = Categoria(nome="Eletrônicos")
    db.add(categoria)
    db.commit()
    db.refresh(categoria)

    produto = crud_produto.criar_produto(db, ProdutoCreate(nome="Notebook", preco=3500.00, categoria_id=categoria.id))

    crud_produto.deletar_produto(db, produto)
    produto_removido = db.query(Produto).filter(Produto.id == produto.id).first()
    assert produto_removido is None