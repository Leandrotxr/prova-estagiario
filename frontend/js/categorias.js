function listarCategorias() {
    fetch(`${API_URL}/categorias/`)
        .then(res => {
            if (!res.ok) throw new Error("Erro ao listar categorias");
            return res.json();
        })
        .then(dados => {
            const lista = document.getElementById("listaCategorias");
            lista.innerHTML = "";

            dados.forEach(cat => {
                const li = document.createElement("li");
                li.textContent = `${cat.id} - ${cat.nome}`;
                lista.appendChild(li);
            });
        })
        .catch(err => {
            console.error(err);
        });
}

function criarCategoria() {
    const nome = document.getElementById("nomeCategoria").value;

    if (!nome) {
        alert("Informe o nome da categoria");
        return;
    }

    fetch(`${API_URL}/categorias/criar_categoria`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ nome })
    })
    .then(res => {
        if (!res.ok) throw new Error("Erro ao criar");
        document.getElementById("nomeCategoria").value = "";
        listarCategorias();
    })
    .catch(err => {
        console.error(err);
    });
}

function buscarCategoria() {
    const id = document.getElementById("buscarId").value;

    if (!id) {
        alert("Informe o ID");
        return;
    }

    fetch(`${API_URL}/categorias/${id}`)
        .then(res => {
            if (!res.ok) throw new Error("Não encontrada");
            return res.json();
        })
        .then(cat => {
            document.getElementById("resultadoBusca").innerText =
                `${cat.id} - ${cat.nome}`;
        })
        .catch(() => {
            document.getElementById("resultadoBusca").innerText =
                "Categoria não encontrada";
        });
}

function deletarCategoria() {
    const id = document.getElementById("deletarId").value;
    const resultado = document.getElementById("resultadoDelete");

    if (!id) {
        alert("Informe o ID");
        return;
    }

    fetch(`${API_URL}/categorias/deletar_categoria`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({id: Number(id)})
    })
        .then(async res => {
            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.detail || "Erro ao deletar categoria");
            }
            return res.json();
        })
        .then(() => {
            resultado.innerText = "Categoria removida com sucesso";
            listarCategorias();
        })
        .catch(err => {
            resultado.innerText = err.message;
        });
}

listarCategorias();