import json

def criar_categoria(client):
    response = client.post(
        "/categorias/criar_categoria",
        json={"nome": "Eletrônicos"}
    )

    assert response.status_code == 201
    return response.json()["id"]


def test_listar_produtos_vazio(client):
    response = client.get("/produtos/")
    assert response.status_code == 200
    assert response.json() == []


def test_criar_produto_sucesso(client):
    categoria_id = criar_categoria(client)

    response = client.post(
        "/produtos/criar_produto",
        json={
            "nome": "Notebook",
            "preco": 3500.00,
            "categoria_id": categoria_id
        }
    )

    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Notebook"
    assert data["preco"] == 3500.00
    assert data["categoria"]["id"] == categoria_id


def test_criar_produto_preco_negativo(client):
    categoria_id = criar_categoria(client)

    response = client.post(
        "/produtos/criar_produto",
        json={
            "nome": "Notebook",
            "preco": -10,
            "categoria_id": categoria_id
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Não é possível colocar um preço menor que 0"


def test_criar_produto_categoria_inexistente(client):
    response = client.post(
        "/produtos/criar_produto",
        json={
            "nome": "Notebook",
            "preco": 3500.00,
            "categoria_id": 999
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Categoria não encontrada"


def test_buscar_produto_por_id(client):
    categoria_id = criar_categoria(client)

    criar = client.post(
        "/produtos/criar_produto",
        json={
            "nome": "Notebook",
            "preco": 3500.00,
            "categoria_id": categoria_id
        }
    )

    produto_id = criar.json()["id"]

    response = client.get(f"/produtos/{produto_id}")

    assert response.status_code == 200
    assert response.json()["id"] == produto_id


def test_buscar_produto_inexistente(client):
    response = client.get("/produtos/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Produto não encontrado"


def test_atualizar_preco_sucesso(client):
    categoria_id = criar_categoria(client)

    criar = client.post(
        "/produtos/criar_produto",
        json={
            "nome": "Notebook",
            "preco": 3500.00,
            "categoria_id": categoria_id
        }
    )

    produto_id = criar.json()["id"]

    response = client.patch(
        "/produtos/atualizar_preco",
        json={
            "id": produto_id,
            "preco": 5000.00
        }
    )

    assert response.status_code == 200
    assert response.json()["preco"] == 5000.00


def test_atualizar_preco_produto_inexistente(client):
    response = client.patch(
        "/produtos/atualizar_preco",
        json={
            "id": 999,
            "preco": 1000.00
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Produto não encontrado"


def test_deletar_produto_sucesso(client):
    categoria_id = criar_categoria(client)

    criar = client.post(
        "/produtos/criar_produto",
        json={
            "nome": "Notebook",
            "preco": 3500.00,
            "categoria_id": categoria_id
        }
    )

    produto_id = criar.json()["id"]

    response = client.request(
        "DELETE",
        "/produtos/deletar_produto",
        data=json.dumps({"id": produto_id}),
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 200
    assert response.json()["msg"] == "Produto removido com sucesso"


def test_deletar_produto_inexistente(client):
    response = client.request(
        "DELETE",
        "/produtos/deletar_produto",
        json={"id": 999}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Produto não encontrado"
