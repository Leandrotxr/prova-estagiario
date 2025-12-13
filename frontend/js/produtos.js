function listarProdutos() {
    fetch(`${API_URL}/produtos/`)
        .then(res => res.json())
        .then(dados => {
            const lista = document.getElementById("listaProdutos");
            lista.innerHTML = "";

            dados.forEach(p => {
                const li = document.createElement("li");
                li.textContent = `${p.nome} - R$ ${p.preco} (${p.categoria.nome})`;
                lista.appendChild(li);
            });
        });
}

function criarProduto() {
    const nome = document.getElementById("nomeProduto").value;
    const preco = Number(document.getElementById("precoProduto").value);
    const categoria_id = Number(document.getElementById("categoriaId").value);

    fetch(`${API_URL}/produtos/criar_produto`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome, preco, categoria_id })
    })
    .then(() => listarProdutos());
}

listarProdutos();
