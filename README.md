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

Configurar o Backend
Instalar dependências:

Certifique-se de ter o Python 3 instalado na sua máquina.
Navegue até a pasta do backend do projeto e crie um ambiente virtual:
bash
Copiar
Editar
python3 -m venv venv
Ative o ambiente virtual:

No Windows:
bash
Copiar
Editar
venv\Scripts\activate
No Mac/Linux:
bash
Copiar
Editar
source venv/bin/activate
Instale as dependências necessárias:

bash
Copiar
Editar
pip install -r requirements.txt
Configurar a API_KEY:

Cadastre-se na OpenWeatherMap e pegue sua chave de API (API_KEY).
Substitua a variável API_KEY no código do backend com sua chave.
3. Rodar o Backend
Na pasta do backend, execute o seguinte comando para rodar o servidor Flask:

bash
Copiar
Editar
python app.py
Isso iniciará o servidor local em http://127.0.0.1:5000.

4. Configurar o Frontend
Navegue até a pasta do frontend do projeto (onde está o arquivo index.html) e abra o arquivo index.html no seu navegador.
O frontend fará requisições ao servidor Flask que você iniciou anteriormente para obter as informações de clima.
5. Como Usar
Abra o arquivo index.html no seu navegador.
Digite o nome de uma cidade na caixa de pesquisa e clique em "Buscar".
O sistema irá retornar a previsão do tempo da cidade informada, incluindo a temperatura e a descrição do clima.
