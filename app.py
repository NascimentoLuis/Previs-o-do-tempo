from flask import Flask, request, jsonify  # Importa as bibliotecas Flask para criar o servidor e manipular requisições
import requests  # Biblioteca para fazer requisições HTTP à API de clima
from flask_cors import CORS  # Importa o CORS para permitir requisições do front-end

app = Flask(__name__)  # Inicializa a aplicação Flask
CORS(app)  # Habilita o CORS para permitir que o front-end acesse este back-end

# Chave da API do OpenWeatherMap (usada para obter dados de clima)
API_KEY = "efdc6be790b13e68bc989f788addc8a7"

# Define a rota "/clima" para responder a requisições GET
@app.route('/clima', methods=['GET'])
def obter_previsao_tempo():
    cidade = request.args.get('cidade')  # Obtém o nome da cidade passada como parâmetro na URL
    
    if not cidade:  # Se a cidade não for informada, retorna um erro
        return jsonify({"erro": "Cidade não informada"}), 400

    # Monta a URL da API do OpenWeatherMap com a cidade informada, a chave da API e configurações de unidade e idioma
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    
    resposta = requests.get(url)  # Faz a requisição para obter os dados do clima

    if resposta.status_code == 200:  # Se a resposta for bem-sucedida
        dados = resposta.json()  # Converte a resposta JSON em um dicionário Python
        
        # Retorna os dados formatados em JSON com a temperatura e a descrição do clima
        return jsonify({
            "cidade": cidade,
            "temperatura": dados["main"]["temp"],  # Obtém a temperatura em graus Celsius
            "descricao": dados["weather"][0]["description"]  # Obtém a descrição do clima (ex: "céu limpo")
        })
    else:
        # Se a cidade não for encontrada, retorna um erro 404
        return jsonify({"erro": "Cidade não encontrada"}), 404

# Inicia o servidor Flask no modo debug, permitindo que o código recarregue automaticamente ao ser modificado
if __name__ == '__main__':
    app.run(debug=True)
