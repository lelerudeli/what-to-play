import mysql.connector

def conexao_abrir(host, usuario, senha, banco, porta):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco,port=porta)

def conexao_fechar(con):
    con.close