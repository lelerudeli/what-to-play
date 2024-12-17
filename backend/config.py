import os
class Config:
    # Configuração do banco de dados
    HOST = "junction.proxy.rlwy.net"
    USER = "root"
    PASSWORD = "utknNNutQbWRwVpeoIiRFrpyCgQtBkEI"
    NAME = "whattoplay"
    PORT = 53813
    
    SECRET_KEY = os.urandom(24)  # Gera uma chave secreta aleatória