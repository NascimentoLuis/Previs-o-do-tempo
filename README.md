# Previsão do Tempo 🌤️

Esse projeto permite que você consulte a previsão do tempo de uma cidade, usando a API do OpenWeatherMap.

## Como instalar e rodar

### Pré-requisitos:
- Python 3.x
- Node.js (caso queira rodar o front-end também)

### Instalação

1. **Clone o repositório para a sua máquina:**

```bash
git clone https://github.com/NascimentoLuis/previsao-do-tempo.git
```

**Configurar o Backend:**
*Instalar dependências:**

Certifique-se de ter o Python 3 instalado na sua máquina.

Navegue até a pasta do backend do projeto e crie um ambiente virtual:
**python3 -m venv venv**

**Ativar o ambiente virtual:**
No Windows: venv\Scripts\activate

**No Mac/Linux**
source venv/bin/activate

**Configurar a API_KEY:**
Cadastre-se na OpenWeatherMap e pegue sua chave de API (API_KEY).
Substitua a variável API_KEY no código do backend (app.py) com sua chave pessoal.

**Rodar o Backend:**
python app.py
Isso iniciará o servidor local em: http://127.0.0.1:5000.

**Configurar o Frontend:**
Navegue até a pasta onde está o arquivo index.html.
Abra o arquivo index.html no seu navegador de preferência.
O frontend fará requisições ao servidor Flask que você iniciou anteriormente para obter as informações de clima.

**Como Usar**
Abra o arquivo index.html no seu navegador.
Digite o nome de uma cidade na caixa de pesquisa e clique em "Buscar".
O sistema irá retornar a previsão do tempo da cidade informada, incluindo a temperatura e a descrição do clima. 

**Estrutura de Arquivos**
index.html: Página principal onde o usuário insere o nome da cidade para buscar a previsão do tempo.
style.css: Estilo da página (interface).
script.js: Código JavaScript que faz a requisição ao backend e manipula a resposta.
app.py: Backend feito em Flask que consome a API OpenWeatherMap e retorna a previsão do tempo.








