function listarCategorias() {
    fetch(`${API_URL}/categorias/`)
        .then(res => res.json())
        .then(dados => {
            const lista = document.getElementById("listaCategorias");
            lista.innerHTML = "";

            dados.forEach(cat => {
                const li = document.createElement("li");
                li.textContent = `${cat.id} - ${cat.nome}`;
                lista.appendChild(li);
            });
        });
}

function criarCategoria() {
    const nome = document.getElementById("nomeCategoria").value;

    fetch(`${API_URL}/categorias/criar_categoria`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nome })
    })
    .then(() => listarCategorias());
}

listarCategorias();
