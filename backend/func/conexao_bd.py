import mysql.connector

def conexao_abrir(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

def conexao_fechar(con):
    con.close