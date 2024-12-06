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



    # Alguma rota que liste todos os usuários (Apenas exemplo)
#    @app.route('/usuarios', methods=['GET'])
#    def listar_todos_usuarios():
#        """Listar todos os usuários"""
#        usuarios = listar_usuarios(app)
#        return jsonify(usuarios)

    # Rota para fazer um select by id (Apenas para exemplo)
#    @app.route('/usuarios/<int:id>', methods=['GET'])
#    def obter_usuario(id):
        """Obter um usuário específico pelo ID"""
#        usuario = obter_usuario_por_id(app, id)
#        if usuario:
#            return jsonify(usuario)
#        return jsonify({'error': 'Usuário não encontrado'}), 404

    # Rota para update do usuário passando o ID (Coloca o ID na rota, ideal seria puxar da própria sessão)
#    @app.route('/usuarios/<int:id>', methods=['PUT'])
#    def atualizar_usuario_existente(id):
        """Atualizar um usuário existente"""
#        usuario_infos = request.json
#        linhas_atualizadas = atualizar_usuario(app, id, usuario_infos)
#        if linhas_atualizadas:
#            return jsonify({'message': 'Usuário atualizado com sucesso'})
#        return jsonify({'error': 'Usuário não encontrado'}), 404

    # Excluir um usuário existente (Espero não precisar usar. Mas é para dar um exemplo da rota de delete)
#    @app.route('/usuarios/<int:id>', methods=['DELETE'])
#    def excluir_usuario_existente(id):
        """Excluir um usuário existente"""
#        linhas_afetadas = excluir_usuario(app, id)
#        if linhas_afetadas:
#            return jsonify({'message': 'Usuário excluído com sucesso'})
#        return jsonify({'error': 'Usuário não encontrado'}), 404

    return app