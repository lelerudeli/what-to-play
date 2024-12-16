from flask import Flask, request, jsonify
from app.dao.usuario_dao import *
from app.dao.jogos_dao import *
from config import Config
from flask_cors import CORS

def iniciar_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Página de cadastro
    @app.route('/cadastro', methods=['POST'])
    def cadastro():
        """Página inicial: cadastro de usuário"""
        usuario_infos = request.json
        if not usuario_infos:
            return jsonify({'erro': 'Dados do usuário não fornecidos.'}), 400

        try:
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

        id_usuario, tipo_usuario = autenticar_usuario(app, login_infos)
        
        if id_usuario:
            return jsonify({
                "mensagem": "Login realizado com sucesso!",
                "id": id_usuario,
                "tipo": tipo_usuario
            }), 200
        else:
            return jsonify({"erro": "E-mail ou senha inválidos."}), 401
        
    @app.route('/esqueci-senha', methods=['POST'])
    def esqueci_senha():
        """Verifica se o e-mail existe no sistema para redefinição de senha."""
        email = request.json
        
        if not email:
            return jsonify({"erro": "E-mail não fornecido."}), 400

        usuario = verificar_email(app, email)
        if usuario:
            return jsonify({
                "mensagem": "E-mail encontrado.",
                "email": usuario['emailUsuario'],
                "id": usuario['idUsuario']
            }), 200
        else:
            return jsonify({"erro": "E-mail não registrado no sistema."}), 404
        
    @app.route('/jogos', methods=['GET'])
    def obter_todos_jogos():
        """Obter todos os jogos."""
        jogos = obter_jogos(app)
        
        if jogos:
            return jsonify(jogos)
        return jsonify({"mensagem": "Nenhum jogo encontrado."}), 200


    @app.route('/jogos/<string:tipo>', methods=['GET'])
    def obter_jogos_por_tipo(tipo):
        """Obter jogos de um tipo específico."""
        if not tipo:
            return jsonify({'erro': 'O tipo do jogo não foi especificado.'}), 400

        jogos = obter_jogo_por_tipo(app, tipo)
        if jogos:
            return jsonify(jogos), 200
        return jsonify({'erro': 'Nenhum jogo encontrado para o tipo especificado.'}), 404

    @app.route('/jogos/<int:id>', methods=['GET'])
    def obter_jogo(id):
        """Obter informações de um jogo específico pelo ID."""
        jogo = obter_jogo_por_id(app, id)
        if jogo:
            return jsonify(jogo), 200
        return jsonify({'erro': 'Jogo com o ID especificado não foi encontrado.'}), 404


    @app.route('/jogos/<int:id>', methods=['PUT'])
    def atualizar_jogo_por_id(id):
        """Atualizar informações de um jogo específico pelo ID."""
        jogo_infos = request.json
        if not jogo_infos:
            return jsonify({'erro': 'Dados para atualização não fornecidos.'}), 400

        linhas_atualizadas = atualizar_jogo(app, id, jogo_infos)
        if linhas_atualizadas > 0:
            return jsonify({'mensagem': 'Jogo atualizado com sucesso!'}), 200
        return jsonify({'erro': 'Jogo não encontrado ou sem alterações realizadas.'}), 404

    @app.route('/jogos/<int:id>', methods=['DELETE'])
    def excluir_jogo_por_id(id):
        """Excluir um jogo específico pelo ID."""
        linhas_afetadas = excluir_jogo(app, id)
        if linhas_afetadas > 0:
            return jsonify({'mensagem': 'Jogo excluído com sucesso!'}), 200
        return jsonify({'erro': 'Jogo com o ID especificado não foi encontrado.'}), 404

    return app