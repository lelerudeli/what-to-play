from whattoplay.application.func.conexao_bd import conexao_abrir, conexao_fechar

# Abrir a conexão
con = conexao_abrir("junction.proxy.rlwy.net", "root", "uXoouZATPTMRXWqFnlUJgRxHozhruwzx", "whattoplay", 59391)

def obter_usuarios(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Usuario")
        return cursor.fetchall()

def obter_jogos(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Jogo")
        return cursor.fetchall()

def obter_avaliacoes(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Avalia")
        return cursor.fetchall()

def obter_favoritos(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Favorita")
        return cursor.fetchall()

def obter_classificacoes_etarias(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM ClassificacaoEtaria")
        return cursor.fetchall()
    
html_usuarios = obter_usuarios(con)
conexao_fechar(con)
