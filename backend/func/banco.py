from conexao_bd import *

con = conexao_abrir("junction.proxy.rlwy.net:59391", "root", "uXoouZATPTMRXWqFnlUJgRxHozhruwzx", "railway")
def listar_usuarios(con):
    cursor = con.cursor(dictionary=True)  # Criar o cursor com a opção de retorno como dicionário
    sqlcode = "SELECT * FROM whattoplay"
    cursor.execute(sqlcode)

    for usuario in cursor:
        print(f"Usuario: {whattoplay['id']} - Email: {whattoplay['email']} ")

    cursor.close()
    con.commit()

listar_usuarios(con)

conexao_fechar(con)

