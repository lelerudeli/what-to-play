from flask import Flask, render_template, request, jsonify, url_for, redirect
from functools import wraps
from whattoplay.application.func.banco import *
from whattoplay.application.func.funcoes import *
from flask_cors import CORS

# Definição de rotas aqui

app = Flask(__name__)
CORS(app)


def requer_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        usuarios = jsonify(obter_usuarios(con))

        if 'usuario_logado' in session:
            usuario = next((user for user in usuarios if user['idUsuario'] == session['usuario_logado']), None)
            if usuario and usuario['tipoUsuario'] == 'admin':
                return f(*args, **kwargs)
        return redirect(url_for('login'))  # Redireciona para login se não for admin
    return decorated_function

@app.route('/')
def index():
    return redirect(url_for('api'))

@app.route('/cadastro')
def cadastro():
    return

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        usuarios = jsonify(obter_usuarios(con))

        nome_usuario = request.form['nomeUsuario']
        senha = request.form['senhaUsuario']
        usuario = next((user for user in usuarios if user['nomeUsuario'] == nome_usuario and user['senhaUsuario'] == senha), None)
        if usuario:
            session['usuario_logado'] = usuario['idUsuario']
            return redirect(url_for('index'))
        else:
            return "Usuário ou senha inválidos."
    return render_template('login.html')

@app.route('/api')
@requer_admin
def api():
    usuarios = jsonify(obter_usuarios(con))
    if 'usuario_logado' in session:
        usuarios = jsonify(obter_usuarios(con))
        usuario = next((user for user in usuarios if user['idUsuario'] == session['usuario_logado']), None)
        return f"Bem-vindo(a), {usuario['nomeCompleto']}!"
    else:
        return redirect(url_for('login'))

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(obter_usuarios(con))

@app.route('/api/jogos', methods=['GET'])
def get_jogos():
    return jsonify(obter_jogos(con))

@app.route('/api/avaliacoes', methods=['GET'])
def get_avaliacoes():
    return jsonify(obter_avaliacoes(con))

@app.route('/api/favoritos', methods=['GET'])
def get_favoritos():
    return jsonify(obter_favoritos(con))

@app.route('/api/classificacoes_etarias', methods=['GET'])
def get_classificacoes_etarias():
    return jsonify(obter_classificacoes_etarias(con))

if __name__ == '__main__':
    app.run(debug=True)
# Definição de rotas com post ou get