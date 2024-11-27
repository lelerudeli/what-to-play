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

def criar_usuario(con, usuario_infos):
    """Insere um novo usuário no banco de dados."""
    
    query = """
    INSERT INTO Usuario (nomeUsuario, nomeCompleto, emailUsuario, tipoUsuario)
    VALUES (%s, %s, %s, %s)
    """
    valores = (
        usuario_infos['nomeUsuario'],
        usuario_infos['nomeCompleto'],
        usuario_infos['emailUsuario'],
        usuario_infos['tipoUsuario']
    )
    
    with con.cursor() as cursor:
        cursor.execute(query, valores)
        con.commit()
        
    return cursor.lastrowid  # Retorna o ID do usuário 

def obter_usuario_por_id(con, id_usuario):
    """Obtém os detalhes de um usuário usando o id."""
    
    query = "SELECT * FROM Usuario WHERE idUsuario = %s"
    
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query, (id_usuario,))
        usuario = cursor.fetchone()

    return usuario

def atualizar_usuario(con, id_usuario, usuario_infos):
    """Atualiza os dados de um usuário existente."""
    
    query = """
    UPDATE Usuario
    SET nomeUsuario = %s, nomeCompleto = %s, emailUsuario = %s, tipoUsuario = %s
    WHERE idUsuario = %s
    """
    valores = (
        usuario_infos['nomeUsuario'],
        usuario_infos['nomeCompleto'],
        usuario_infos['emailUsuario'],
        usuario_infos['tipoUsuario'],
        id_usuario
    )
    
    with con.cursor() as cursor:
        cursor.execute(query, valores)
        con.commit()
        

def excluir_usuario(con, id_usuario):
    """Remove um usuário do banco de dados."""
    query = "DELETE FROM Usuario WHERE idUsuario = %s"
    
    with con.cursor() as cursor:
        cursor.execute(query, (id_usuario,))
        con.commit()
    
html_usuarios = obter_usuarios(con)
conexao_fechar(con)
