from flask import Flask, request, jsonify
from app.dao.usuario_dao import *
from app.dao.jogos_dao import *
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

def iniciar_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    jwt = JWTManager(app)
    
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
                
            novo_id, tipo_usuario = criar_usuario(app, usuario_infos)
            
            # Cria o token JWT com as informações do usuário
            access_token = create_access_token(identity={"id": novo_id,"tipo": tipo_usuario, "nome": usuario_infos.get('nomeUsuario') })
        
            return jsonify({'id': novo_id, 'mensagem': 'Usuário cadastrado com sucesso!', 'token': access_token}), 201
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
            # Cria o token JWT com informações do usuário
            access_token = create_access_token(identity={"id": id_usuario,"tipo": tipo_usuario, "nome": nome_usuario })
            return jsonify({
                "mensagem": "Login realizado com sucesso!",
                "token": access_token
            }), 200
        else:
            return jsonify({"erro": "E-mail ou senha inválidos."}), 401
        
        # Página de logout
    @app.route('/logout', methods=['DELETE'])
    def logout():
        """Faz logout do usuário e limpa a sessão."""
        #No backend, o jwt não precisa fazer nada
        return jsonify({"mensagem": "Logout realizado com sucesso!"}), 200
        
    @app.route('/jogos', methods=['GET'])
    def obter_todos_jogos():
        """Obter todos os jogos."""
        jogos = obter_jogos(app)
        
        if jogos:
            return jsonify(jogos)
        return jsonify({"mensagem": "Nenhum jogo encontrado."}), 200

    @app.route('/perfil', methods = ['GET'])
    @jwt_required()
    def obter_dados_usuario():
        """Obter dados do usuário para o perfil"""
        current_user = get_jwt_identity()  # Obtém informações do token
        id_usuario = current_user["id"]
        usuario = obter_usuario_por_id(app, id_usuario)


        if usuario:
            return jsonify(usuario), 200  
        else:
            return jsonify({"erro": "Usuário não encontrado."}), 404
        
    return app