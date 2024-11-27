from flask import Flask, request, jsonify
from app.dao.usuario_dao import listar_usuarios, criar_usuario, obter_usuario_por_id, atualizar_usuario, excluir_usuario
from config import Config
from flask_cors import CORS

def iniciar_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Página ininicial (Faz o cadastro)
    @app.route('/', methods=['POST'])
    def cadastrar_usuario():
        """Página inicial: cadastro de usuário"""
        usuario_infos = request.json
        novo_id = criar_usuario(app, usuario_infos)
        return jsonify({'id': novo_id}), 201

    # Alguma rota que liste todos os usuários (Apenas exemplo)
    @app.route('/usuarios', methods=['GET'])
    def listar_todos_usuarios():
        """Listar todos os usuários"""
        usuarios = listar_usuarios(app)
        return jsonify(usuarios)

    # Rota para fazer um select by id (Apenas para exemplo)
    @app.route('/usuarios/<int:id>', methods=['GET'])
    def obter_usuario(id):
        """Obter um usuário específico pelo ID"""
        usuario = obter_usuario_por_id(app, id)
        if usuario:
            return jsonify(usuario)
        return jsonify({'error': 'Usuário não encontrado'}), 404

    # Rota para update do usuário passando o ID (Coloca o ID na rota, ideal seria puxar da própria sessão)
    @app.route('/usuarios/<int:id>', methods=['PUT'])
    def atualizar_usuario_existente(id):
        """Atualizar um usuário existente"""
        usuario_infos = request.json
        linhas_atualizadas = atualizar_usuario(app, id, usuario_infos)
        if linhas_atualizadas:
            return jsonify({'message': 'Usuário atualizado com sucesso'})
        return jsonify({'error': 'Usuário não encontrado'}), 404

    # Excluir um usuário existente (Espero não precisar usar. Mas é para dar um exemplo da rota de delete)
    @app.route('/usuarios/<int:id>', methods=['DELETE'])
    def excluir_usuario_existente(id):
        """Excluir um usuário existente"""
        linhas_afetadas = excluir_usuario(app, id)
        if linhas_afetadas:
            return jsonify({'message': 'Usuário excluído com sucesso'})
        return jsonify({'error': 'Usuário não encontrado'}), 404

    return app