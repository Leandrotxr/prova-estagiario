function listarProdutos() {
    fetch(`${API_URL}/produtos/`)
        .then(res => {
            if (!res.ok) throw new Error("Erro ao listar produtos");
            return res.json();
        })
        .then(dados => {
            const lista = document.getElementById("listaProdutos");
            lista.innerHTML = "";

            dados.forEach(p => {
                const li = document.createElement("li");
                li.textContent = `${p.id} - ${p.nome} | R$ ${p.preco} | Categoria: ${p.categoria.nome}`;
                lista.appendChild(li);
            });
        })
        .catch(err => {
            console.error(err);
        });
}

function criarProduto() {
    const nome = document.getElementById("nomeProduto").value;
    const preco = document.getElementById("precoProduto").value;
    const categoria_id = document.getElementById("categoriaIdProduto").value;

    if (!nome || !preco || !categoria_id) {
        alert("Preencha todos os campos");
        return;
    }

    fetch(`${API_URL}/produtos/criar_produto`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nome,
            preco: Number(preco),
            categoria_id: Number(categoria_id)
        })
    })
    .then(res => {
        if (!res.ok) throw new Error("Erro ao criar produto");
        document.getElementById("nomeProduto").value = "";
        document.getElementById("precoProduto").value = "";
        document.getElementById("categoriaIdProduto").value = "";
        listarProdutos();
    })
    .catch(err => {
        console.error(err);
    });
}

function buscarProduto() {
    const id = document.getElementById("buscarProdutoId").value;

    if (!id) {
        alert("Informe o ID");
        return;
    }

    fetch(`${API_URL}/produtos/${id}`)
        .then(res => {
            if (!res.ok) throw new Error("Produto não encontrado");
            return res.json();
        })
        .then(p => {
            document.getElementById("resultadoBuscaProduto").innerText =
                `${p.id} - ${p.nome} | R$ ${p.preco} | Categoria: ${p.categoria.nome}`;
        })
        .catch(() => {
            document.getElementById("resultadoBuscaProduto").innerText =
                "Produto não encontrado";
        });
}

function atualizarPreco() {
    const id = document.getElementById("atualizarProdutoId").value;
    const preco = document.getElementById("novoPrecoProduto").value;

    if (!id || !preco) {
        alert("Informe o ID e o novo preço");
        return;
    }

    fetch(`${API_URL}/produtos/atualizar_preco`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            id: Number(id),
            preco: Number(preco)
        })
    })
    .then(res => {
        if (!res.ok) throw new Error("Erro ao atualizar preço");
        document.getElementById("resultadoAtualizarPreco").innerText =
            "Preço atualizado com sucesso";
        listarProdutos();
    })
    .catch(() => {
        document.getElementById("resultadoAtualizarPreco").innerText =
            "Erro ao atualizar preço";
    });
}

function deletarProduto() {
    const id = document.getElementById("deletarProdutoId").value;

    if (!id) {
        alert("Informe o ID");
        return;
    }

    fetch(`${API_URL}/produtos/deletar_produto`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id: Number(id) })
    })
    .then(res => {
        if (!res.ok) throw new Error("Erro ao deletar produto");
        document.getElementById("resultadoDeleteProduto").innerText =
            "Produto removido com sucesso";
        listarProdutos();
    })
    .catch(() => {
        document.getElementById("resultadoDeleteProduto").innerText =
            "Erro ao deletar produto";
    });
}

listarProdutos();
