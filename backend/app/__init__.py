from flask import Flask, render_template
from app.dao.usuario_dao import lista_usuarios, listar_usuarios
from config import Config 

def iniciar_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    @app.route('/')
    def usuarios():
        print("Rota /usuarios chamada!")  
        usuarios = listar_usuarios(app)
        html_usuarios = lista_usuarios(usuarios)

        return render_template('user.html', usuarios_html=html_usuarios)
        
    return app
    
    

