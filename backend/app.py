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
        username = request.form.get('username')
        password = request.form.get('password')
        usuarios = (obter_usuarios(con))
        print(usuarios)
        for user in usuarios:
            if user['idUsuario'] == username:
                id = user['idUsuario']
                return jsonify(obter_usuario_por_id(con, id))
    else:
            return "Usuário invalido"
    
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

# Página de cadastro
    @app.route('/cadastro', methods=['POST'])
    def cadastro():
        """Página inicial: cadastro de usuário"""
        usuario_infos = request.json
        novo_id = criar_usuario(app, usuario_infos)
        return jsonify({'id': novo_id}), 201
    
    # Página de login
    @app.route('/login', methods=['POST'])
    def login():
        """Endpoint para autenticação de usuário."""
        login_infos = request.json
        id_usuario = autenticar_usuario(app, login_infos)

        if id_usuario:
            return jsonify({"mensagem": "Login realizado com sucesso!", "id": id_usuario}), 200
        else:
            return jsonify({"erro": "Credenciais inválidas!"}), 401
        
    @app.route('/esqueci-senha', methods=['POST'])
    def esqueci_senha():
        """Verifica se o e-mail existe no sistema para redefinição de senha."""
        email = request.json
        
        if not email:
            return jsonify({"erro": "E-mail não fornecido."}), 400
        
        # Verificar se o e-mail existe no banco de dados
        usuario = verificar_email(app, email)

        if usuario:
            return jsonify({
                "mensagem": "E-mail encontrado.",
                "email": usuario['emailUsuario'],  # Retorna o e-mail para o próximo passo
                "id": usuario['idUsuario']        # Retorna o ID para identificar o usuário
            }), 200
        else:
            return jsonify({"erro": "E-mail não encontrado."}), 404
        
    @app.route('/jogos', methods=['GET'])
    def obter_todos_jogos():
        """Obter todos os jogos."""
        jogos = obter_jogos(app)
        
        if jogos:
            return jsonify(jogos)
        return jsonify({'error': 'Nenhum jogo encontrado'}), 404

    @app.route('/jogos/<string:tipo>', methods=['GET'])
    def obter_jogos_por_tipo(tipo):
        """Obter jogos de um tipo específico."""
        jogos = obter_jogo_por_tipo(app, tipo)
        
        if jogos:
            return jsonify(jogos)
        return jsonify({'error': 'Nenhum jogo encontrado para o tipo especificado'}), 404
    
    @app.route('/jogos/<int:id>', methods=['GET'])
    def obter_jogo(id):
        """Obter informações de um jogo específico pelo ID."""
        jogo = obter_jogo_por_id(app, id)
        
        if jogo:
            return jsonify(jogo)
        return jsonify({'error': 'Jogo não encontrado'}), 404

    @app.route('/jogos/<int:id>', methods=['PUT'])
    def atualizar_jogo_por_id(id):
        """Atualizar informações de um jogo específico pelo ID."""
        jogo_infos = request.json

        linhas_atualizadas = atualizar_jogo(app, id, jogo_infos)
        if linhas_atualizadas > 0:
            return jsonify({'message': 'Jogo atualizado com sucesso'}), 200
        return jsonify({'error': 'Jogo não encontrado ou sem alterações'}), 404
  
    @app.route('/jogos/<int:id>', methods=['DELETE'])
    def excluir_jogo_por_id(id):
        """Excluir um jogo específico pelo ID."""
        linhas_afetadas = excluir_jogo(app, id)
        if linhas_afetadas > 0:
            return jsonify({'message': 'Jogo excluído com sucesso'}), 200
        return jsonify({'error': 'Jogo não encontrado'}), 404



if __name__ == '__main__':
    app.run(debug=True)
# Definição de rotas com post ou get