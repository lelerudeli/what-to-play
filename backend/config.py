import os
class Config:
    # Configuração do banco de dados
    HOST = "junction.proxy.rlwy.net"
    USER = "root"
    PASSWORD = "utknNNutQbWRwVpeoIiRFrpyCgQtBkEI"
    NAME = "whattoplay"
    PORT = 53813
    
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = os.urandom(24)  # Chave para assinar os tokens
    JWT_ACCESS_TOKEN_EXPIRES = 3600 # 1 hora de sessão
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'seu_email@gmail.com'
    MAIL_PASSWORD = 'sua_senha_do_email'
    MAIL_DEFAULT_SENDER = 'seu_email@gmail.com'