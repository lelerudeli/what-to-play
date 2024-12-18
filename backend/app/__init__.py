import json
from flask import Flask, request, jsonify
from app.dao.usuario_dao import *
from app.dao.jogos_dao import *
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_mail import Mail, Message
from datetime import timedelta

def iniciar_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    jwt = JWTManager(app)
    mail = Mail(app)  


    # Página de cadastro
    @app.route('/cadastrar/usuario', methods=['POST'])
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
            access_token = create_access_token(identity=json.dumps({"id": novo_id, "tipo": tipo_usuario, "nome": usuario_infos.get('nomeUsuario')}))

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
            access_token = create_access_token(identity=json.dumps({"id": id_usuario, "tipo": tipo_usuario, "nome": nome_usuario}))
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
    
    @app.route('/cadastrar/jogo', methods=['POST'])
    @jwt_required() #Obrigatório autenticar para acessar essa rota
    def criar_jogo():
        """Criação de um novo jogo."""
        usuario_logado = json.loads(get_jwt_identity())  # Obtém o usuário logado através do token
        jogo_infos = request.json  
        
        if not jogo_infos:
            return jsonify({"erro": "Dados do jogo não fornecido."}), 400
        
        # Adiciona o ID do usuário logado ao jogos_infos
        jogo_infos['Usuario_idUsuario'] = usuario_logado["id"]

        try:
            novo_jogo_id = criar_jogo(app, jogo_infos)
            return jsonify({
                "mensagem": "Jogo criado com sucesso!",
                "idJogo": novo_jogo_id
            }), 201
        except Exception as e:
            return jsonify({
                "erro": "Erro ao criar o jogo.",
                "detalhes": str(e)
            }), 500
    
    @app.route('/perfil', methods = ['GET'])
    @jwt_required()
    def obter_dados_usuario():
        """Obter dados do usuário para o perfil"""
        
        usuario_logado = json.loads(get_jwt_identity())# Obtém informações do token
        if 'id' not in usuario_logado:
            return jsonify({"erro": "Token inválido, 'id' não encontrado."}), 400
    
        id_usuario = usuario_logado["id"]
        usuario = obter_usuario_por_id(app, id_usuario)
        if usuario:
            return jsonify(usuario), 200  
        else:
            return jsonify({"erro": "Usuário não encontrado."}), 404
        
    @app.route('/redefinir/senha', methods=['POST'])
    def redefinir_senha():
        """Enviar um e-mail para redefinir a senha."""
        email = request.json.get('emailUsuario')
        
        if not email:
            return jsonify({"erro": "E-mail não fornecido."}), 400
        
        usuario_existe = verificar_email(app, email)  
        
        if not usuario_existe:
            return jsonify({"erro": "E-mail não encontrado."}), 404
        
        nome_usuario_upper = usuario_existe['nomeUsuario'].upper()
        
        try:
            msg = Message(
                subject="Redefinição de Senha",
                recipients=[email],
                body=f"Olá, {usuario_existe['nomeUsuario']}!\n\n"
                     f"Isso é um teste para Redefinição de Senha:\n\n"
                     f"Código: TESTE {nome_usuario_upper}\n\n"
                     "Se você não solicitou a redefinição, ignore este e-mail."
            )
            mail.send(msg)

            return jsonify({"mensagem": "E-mail de redefinição enviado com sucesso."}), 200
        except Exception as e:
            return jsonify({"erro": "Erro ao enviar e-mail.", "detalhes": str(e)}), 500
    
        
    return app