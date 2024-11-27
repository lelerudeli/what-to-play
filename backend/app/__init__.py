from flask import Flask, render_template
from app.dao.avalia_dao import lista_avaliacoes, listar_avaliacoes
from app.dao.classificação_etaria_dao import lista_classificacoes_etarias, listar_classificacoes_etarias
from app.dao.favorita_dao import lista_favoritos, listar_favoritos
from app.dao.jogos_dao import lista_jogos, listar_jogos
from app.dao.usuario_dao import lista_usuarios, listar_usuarios
from config import Config 
from flask_cors import CORS

def iniciar_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    
    @app.route('/')
    def usuarios():
        """Rota principal que exibe todos os dados em uma única página"""
        # Obter os dados de cada tabela
        usuarios = listar_usuarios(app)
        jogos = listar_jogos(app)
        avaliacoes = listar_avaliacoes(app)
        favoritos = listar_favoritos(app)
        classificacoes_etarias = listar_classificacoes_etarias(app)

        # Gerar os HTMLs
        html_usuarios = lista_usuarios(usuarios)
        html_jogos = lista_jogos(jogos)
        html_avaliacoes = lista_avaliacoes(avaliacoes)
        html_favoritos = lista_favoritos(favoritos)
        html_classificacoes_etarias = lista_classificacoes_etarias(classificacoes_etarias)
        
        return render_template(
            'index.html',
            usuarios_html=html_usuarios,
            jogos_html=html_jogos,
            avaliacoes_html=html_avaliacoes,
            favoritos_html=html_favoritos,
            classificacoes_etarias_html=html_classificacoes_etarias
        )

    return app