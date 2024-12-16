from flask import Flask, render_template, request, jsonify, url_for, redirect, session, make_response
from functools import wraps
from whattoplay.application.func.banco import *
from whattoplay.application.func.funcoes import *
from flask_cors import CORS

# Definição de rotas aqui

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return redirect(url_for('api'))

@app.route('/api')
def api():
    return render_template('index.html')

@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = obter_usuarios(con)
    response = make_response(jsonify(usuarios))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/api/jogos', methods=['GET'])
def get_jogos():
    jogos = obter_jogos(con)
    response = make_response(jsonify(jogos))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/api/avaliacoes', methods=['GET'])
def get_avaliacoes():
    avaliacoes = obter_avaliacoes(con)
    response = make_response(jsonify(avaliacoes))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/api/favoritos', methods=['GET'])
def get_favoritos():
    favoritos = obter_favoritos(con)
    response = make_response(jsonify(favoritos))
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/api/classificacoes_etarias', methods=['GET'])
def get_classificacoes_etarias():
    classificacoes = obter_classificacoes_etarias(con)
    response = make_response(jsonify(classificacoes))
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/cadastro', methods=['POST'])
def cadastro():
    """Página inicial: cadastro de usuário"""
    try:
        usuario_infos = request.get_json()
        novo_id = criar_usuario(con, usuario_infos)

        response = make_response(jsonify({'id': novo_id}))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 201  # Created
        return response

    except Exception as e:
        # Tratar exceções e retornar um erro 500
        response = make_response(jsonify({'error': 'Erro ao criar usuário'}))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 500  # Internal Server Error
        return response

# Página de login
@app.route('/login', methods=['POST'])
def login():
    """Endpoint para autenticação de usuário."""
    try:
        login_infos = request.get_json()
        id_usuario = autenticar_usuario(con, login_infos)

        if id_usuario:
            response = make_response(jsonify({"mensagem": "Login realizado com sucesso!", "id": id_usuario}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 200  # OK
            return response
        else:
            response = make_response(jsonify({"erro": "Credenciais inválidas!"}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 401  # Unauthorized
            return response

    except Exception as e:
        # Tratar exceções e retornar um erro 500
        response = make_response(jsonify({'error': 'Erro ao processar login'}))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 500  # Internal Server Error
        return response
    
@app.route('/esqueci-senha', methods=['POST'])
def esqueci_senha():
    """Verifica se o e-mail existe no sistema para redefinição de senha."""
    try:
        email = request.get_json()

        if not email:
            response = make_response(jsonify({"erro": "E-mail não fornecido."}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 400  # Bad Request
            return response

        # Verificar se o e-mail existe no banco de dados
        usuario = verificar_email(con, email)

        if usuario:
            response = make_response(jsonify({
                "mensagem": "E-mail encontrado.",
                "email": usuario['emailUsuario'],
                "id": usuario['idUsuario']
            }))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 200  # OK
            return response
        else:
            response = make_response(jsonify({"erro": "E-mail não encontrado."}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 404  # Not Found
            return response

    except Exception as e:
        # Tratar exceções e retornar um erro 500
        response = make_response(jsonify({'error': 'Erro ao processar a solicitação'}))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 500  # Internal Server Error
        return response
    
@app.route('/jogos', methods=['GET'])
def obter_todos_jogos():
    """Obter todos os jogos."""
    try:
        jogos = obter_jogos(con)

        if jogos:
            response = make_response(jsonify(jogos))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 200  # OK
            return response
        else:
            response = make_response(jsonify({'error': 'Nenhum jogo encontrado'}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 404  # Not Found
            return response

    except Exception as e:
        # Tratar exceções e retornar um erro 500
        response = make_response(jsonify({'error': 'Erro ao obter jogos'}))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 500  # Internal Server Error
        return response

@app.route('/jogos/<string:tipo>', methods=['GET'])
def obter_jogos_por_tipo(tipo):
    """Obter jogos de um tipo específico."""
    try:
        jogos = obter_jogo_por_tipo(con, tipo)

        if jogos:
            response = make_response(jsonify(jogos))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 200  # OK
            return response
        else:
            response = make_response(jsonify({'error': 'Nenhum jogo encontrado para o tipo especificado'}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 404  # Not Found
            return response

    except Exception as e:
        # Tratar exceções e retornar um erro 500
        response = make_response(jsonify({'error': 'Erro ao obter jogos'}))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 500  # Internal Server Error
        return response
    

@app.route('/jogos/<int:id>', methods=['GET'])
def obter_jogo(id):
    """Obter informações de um jogo específico pelo ID."""
    try:
        jogo = obter_jogo_por_id(con, id)

        if jogo:
            response = make_response(jsonify(jogo))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 200  # OK
            return response
        else:
            response = make_response(jsonify({'error': 'Jogo não encontrado'}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 404  # Not Found
            return response

    except Exception as e:
        # Tratar exceções e retornar um erro 500
        response = make_response(jsonify({'error': 'Erro ao obter jogo'}))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 500  # Internal Server Error
        return response
    
@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo_por_id(id):
    """Atualizar informações de um jogo específico pelo ID."""
    try:
        jogo_infos = request.get_json()

        linhas_atualizadas = atualizar_jogo(con, id, jogo_infos)

        if linhas_atualizadas > 0:
            response = make_response(jsonify({'message': 'Jogo atualizado com sucesso'}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 200  # OK
            return response
        else:
            response = make_response(jsonify({'error': 'Jogo não encontrado ou sem alterações'}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 404  # Not Found
            return response

    except Exception as e:
        # Tratar exceções e retornar um erro 500
        response = make_response(jsonify({'error': 'Erro ao atualizar jogo'}))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 500  # Internal Server Error
        return response

@app.route('/jogos/<int:id>', methods=['DELETE'])
def excluir_jogo_por_id(id):
    """Excluir um jogo específico pelo ID."""
    try:
        linhas_afetadas = excluir_jogo(con, id)

        if linhas_afetadas > 0:
            response = make_response(jsonify({'message': 'Jogo excluído com sucesso'}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 200  # OK
            return response
        else:
            response = make_response(jsonify({'error': 'Jogo não encontrado'}))
            response.headers['Content-Type'] = 'application/json'
            response.status_code = 404  # Not Found
            return response

    except Exception as e:
        # Tratar exceções e retornar um erro 500
        response = make_response(jsonify({'error': 'Erro ao excluir jogo'}))
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 500  # Internal Server Error
        return response



if __name__ == '__main__':
    app.run(debug=True)
# Definição de rotas com post ou get