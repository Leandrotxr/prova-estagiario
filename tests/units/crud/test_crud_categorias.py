from app.crud import categoria as crud_categoria
from app.schemas.categoria import CategoriaCreate

def test_criar_categoria(db):
    dados = CategoriaCreate(nome="Eletrônicos")

    categoria = crud_categoria.criar_categoria(db, dados)

    assert categoria.id is not None
    assert categoria.nome == "Eletrônicos"

def test_listar_categorias(db):
    crud_categoria.criar_categoria(db, CategoriaCreate(nome="Eletrônicos"))
    crud_categoria.criar_categoria(db, CategoriaCreate(nome="Roupas"))

    categorias = crud_categoria.listar_categorias(db)

    assert len(categorias) == 2
    assert categorias[0].nome == "Eletrônicos"
    assert categorias[1].nome == "Roupas"

def test_buscar_categoria_existente(db):
    categoria_criada = crud_categoria.criar_categoria(db, CategoriaCreate(nome="Eletrônicos"))

    categoria = crud_categoria.buscar_categoria(db, categoria_criada.id)

    assert categoria is not None
    assert categoria.id == categoria_criada.id
    assert categoria.nome == "Eletrônicos"

def test_buscar_categoria_inexistente(db):
    categoria = crud_categoria.buscar_categoria(db, 999)

    assert categoria is None

def test_deletar_categoria(db):
    categoria_criada = crud_categoria.criar_categoria(db, CategoriaCreate(nome="Eletrônicos"))

    crud_categoria.deletar_categoria(db, categoria_criada)

    categoria = crud_categoria.buscar_categoria(db, categoria_criada.id)
    assert categoria is None