import json

def test_listar_categoria_vazio(client):
    response = client.get("/categorias/")
    assert response.status_code == 200
    assert response.json() == []


def test_criar_categoria_sucesso(client):
    response = client.post(
        "/categorias/criar_categoria",
        json={
            "nome": "Eletrônico"
        }
    )

    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Eletrônico"

def test_buscar_categoria_por_id(client):
    criar = client.post(
        "/categorias/criar_categoria",
        json={
            "nome": "Eletrônico"
        }
    )

    categoria_id = criar.json()["id"]

    response = client.get(f"/categorias/{categoria_id}")

    assert response.status_code == 200
    assert response.json()["id"] == categoria_id


def test_buscar_categoria_inexistente(client):
    response = client.get("/categoria/999")

    assert response.status_code == 404

def test_deletar_categoria_sucesso(client):
    criar = client.post(
        "/categorias/criar_categoria",
        json={
            "nome": "Eletrônico"
        }
    )

    categoria_id = criar.json()["id"]

    response = client.request(
        "DELETE",
        "/categorias/deletar_categoria",
        data=json.dumps({"id": categoria_id}),
        headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 200
    assert response.json()["msg"] == "Categoria removida com sucesso"


def test_deletar_produto_inexistente(client):
    response = client.request(
        "DELETE",
        "/categorias/deletar_categoria",
        json={"id": 999}
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Categoria não encontrada"