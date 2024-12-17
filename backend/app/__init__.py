from flask import Flask, request, jsonify
from app.dao.usuario_dao import *
from app.dao.jogos_dao import *
from config import Config
from flask_cors import CORS
from flask import session

def iniciar_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Página de cadastro
    @app.route('/cadastro', methods=['POST'])
    def cadastro():
        """Página inicial: cadastro de usuário"""
        usuario_infos = request.json
        email = usuario_infos.get('emailUsuario')
        
        try:
            usuario_existe = verificar_email(app, email)
            if usuario_existe:
                return jsonify({'erro': 'E-mail já cadastrado.','idUsuario': usuario_existe['idUsuario'],}), 409
                
            novo_id = criar_usuario(app, usuario_infos)
            return jsonify({'id': novo_id, 'mensagem': 'Usuário cadastrado com sucesso!'}), 201
        except Exception as e:
            return jsonify({'erro': 'Erro ao cadastrar o usuário.', 'detalhes': str(e)}), 500

    
    # Página de login
    @app.route('/login', methods=['POST'])
    def login():
        """Endpoint para autenticação de usuário."""
        login_infos = request.json
        if not login_infos:
            return jsonify({'erro': 'Credenciais não fornecidas.'}), 400

        nome_usuario, id_usuario, tipo_usuario = autenticar_usuario(app, login_infos)
        
        if id_usuario:
            # Armazena os dados na sessão
            session["nome_usuario"] = nome_usuario
            session["id_usuario"] = id_usuario
            session["tipo_usuario"] = tipo_usuario
            
            return jsonify({
                "mensagem": "Login realizado com sucesso!",
                "nome": nome_usuario,
                "id": id_usuario,
                "tipo": tipo_usuario
                
            }), 200
        else:
            return jsonify({"erro": "E-mail ou senha inválidos."}), 401
        
        # Página de logout
    @app.route('/logout', methods=['DELETE'])
    def logout():
        """Faz logout do usuário e limpa a sessão."""
        session.clear()
        return jsonify({"mensagem": "Logout realizado com sucesso!"}), 200
        
    @app.route('/jogos', methods=['GET'])
    def obter_todos_jogos():
        """Obter todos os jogos."""
        jogos = obter_jogos(app)
        
        if jogos:
            return jsonify(jogos)
        return jsonify({"mensagem": "Nenhum jogo encontrado."}), 200

    return app