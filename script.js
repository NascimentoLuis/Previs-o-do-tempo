function buscarClima() {
    let cidade = document.getElementById("cidade").value;  // Obtém o valor digitado no input

    // Verifica se o usuário digitou uma cidade
    if (cidade === "") {
        alert("Por favor, digite uma cidade!");  // Exibe um alerta se o campo estiver vazio
        return;  // Encerra a função para evitar requisições desnecessárias
    }

    // Faz uma requisição para o servidor Flask passando a cidade como parâmetro na URL
    fetch(`http://127.0.0.1:5000/clima?cidade=${encodeURIComponent(cidade)}`)
        .then(response => response.json())  // Converte a resposta para JSON
        .then(data => {
            if (data.erro) {  // Se o servidor retornar um erro (ex: cidade não encontrada)
                document.getElementById("resultado").innerHTML = `<p style="color:red;">${data.erro}</p>`;
            } else {
                // Atualiza o conteúdo da div "resultado" com as informações do clima
                document.getElementById("resultado").innerHTML = `
                    <p><strong>Cidade:</strong> ${data.cidade}</p>
                    <p><strong>Temperatura:</strong> ${data.temperatura}°C</p>
                    <p><strong>Descrição:</strong> ${data.descricao}</p>
                `;
            }
        })
        .catch(error => {
            // Se houver um erro na requisição (ex: servidor offline), exibe uma mensagem de erro
            document.getElementById("resultado").innerHTML = `<p style="color:red;">Erro ao obter dados.</p>`;
        });
}
