# 📦 Backend – Sistema de Produtos e Categorias

Este projeto é um backend simples em Python desenvolvido com FastAPI e SQLite, com foco em demonstrar conceitos básicos de API REST, banco de dados relacional e organização de código.

O sistema permite realizar um **CRUD completo** (Criar, Listar, Buscar, Atualizar e Deletar) de **Produtos** e **Categorias**, respeitando o relacionamento:

* Uma Categoria pode ter vários Produtos
* Um Produto pertence a apenas uma Categoria

---

## 🚀 Tecnologias utilizadas

* **Python 3.13**
* **FastAPI** – framework web
* **SQLAlchemy** – ORM
* **Pydantic** – validação de dados
* **SQLite** – banco de dados
* **Uvicorn** – servidor ASGI

---

## 📁 Estrutura do projeto

```
app/
├── core/        # Configurações do projeto (ex: banco)
├── db/          # Base e sessão do banco de dados
├── models/      # Models SQLAlchemy (Produto e Categoria)
├── schemas/     # Schemas Pydantic (entrada e saída de dados)
├── crud/        # Funções de acesso ao banco (CRUD)
├── router/      # Rotas da API (produtos e categorias)
├── main.py      # Arquivo principal da aplicação
└── app.db       # Banco SQLite (gerado automaticamente)
```

---

## ▶️ Como rodar o projeto

### 1️⃣ Criar e ativar o ambiente virtual

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux / Mac:

```bash
source .venv/bin/activate
```

---

### 2️⃣ Instalar as dependências

```bash
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv
```

---

### 3️⃣ Rodar a aplicação

Na raiz do projeto:

```bash
uvicorn app.main:app --reload
```

Saída esperada:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## 🔄 Resetar o banco de dados

O banco é um arquivo SQLite (`app.db`).

Para **zerar todos os dados**:

1. Pare o servidor
2. Apague o arquivo `app.db`
3. Suba a aplicação novamente

O banco será recriado automaticamente.

---

## 👤 Autor

Projeto desenvolvido por **Leandro Teixeira** para fins de estudo e avaliação técnica.
