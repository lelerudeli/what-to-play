from flask import Flask, render_template, request, jsonify
from whattoplay.application.func.banco import *
from flask_cors import CORS

# Definição de rotas aqui

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Retorna uma página HTML com links para todas as rotas da API."""
    return render_template('index.html')

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(obter_usuarios(con))

@app.route('/jogos', methods=['GET'])
def get_jogos():
    return jsonify(obter_jogos(con))

@app.route('/avaliacoes', methods=['GET'])
def get_avaliacoes():
    return jsonify(obter_avaliacoes(con))

@app.route('/favoritos', methods=['GET'])
def get_favoritos():
    return jsonify(obter_favoritos(con))

@app.route('/classificacoes_etarias', methods=['GET'])
def get_classificacoes_etarias():
    return jsonify(obter_classificacoes_etarias(con))

if __name__ == '__main__':
    app.run(debug=True)
# Definição de rotas com post ou get