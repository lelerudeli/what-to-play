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