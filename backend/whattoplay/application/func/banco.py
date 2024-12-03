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
        
def obter_jogos(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Jogo")
        return cursor.fetchall()  

def obter_jogo_por_id(con, id_jogo):
    query = "SELECT * FROM Jogo WHERE idJogo = %s"
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query, (id_jogo,))
        return cursor.fetchone()

def criar_jogo(con, jogo_infos):
    query = """
    INSERT INTO Jogo (
        nomeJogo, regraJogo, tipoJogo, faixaEtaria, 
        numeroCurtidas, numeroJogadores, 
        Usuario_idUsuario, ClassificacaoEtaria_idClassificacao
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        jogo_infos['nomeJogo'],
        jogo_infos['regraJogo'],
        jogo_infos['tipoJogo'],
        jogo_infos['faixaEtaria'],
        jogo_infos['numeroCurtidas'],
        jogo_infos['numeroJogadores'],
        jogo_infos['Usuario_idUsuario'],
        jogo_infos['ClassificacaoEtaria_idClassificacao']
    )
    with con.cursor() as cursor:
        cursor.execute(query, valores)
        con.commit()
    return cursor.lastrowid

def atualizar_jogo(con, id_jogo, jogo_infos):
    query = """
    UPDATE Jogo
    SET nomeJogo = %s, regraJogo = %s, tipoJogo = %s, faixaEtaria = %s, 
        numeroCurtidas = %s, numeroJogadores = %s, 
        Usuario_idUsuario = %s, ClassificacaoEtaria_idClassificacao = %s
    WHERE idJogo = %s
    """
    valores = (
        jogo_infos['nomeJogo'],
        jogo_infos['regraJogo'],
        jogo_infos['tipoJogo'],
        jogo_infos['faixaEtaria'],
        jogo_infos['numeroCurtidas'],
        jogo_infos['numeroJogadores'],
        jogo_infos['Usuario_idUsuario'],
        jogo_infos['ClassificacaoEtaria_idClassificacao'],
        id_jogo
    )
    with con.cursor() as cursor:
        cursor.execute(query, valores)
        con.commit()

def excluir_jogo(con, id_jogo):
    query = "DELETE FROM Jogo WHERE idJogo = %s"
    with con.cursor() as cursor:
        cursor.execute(query, (id_jogo,))
        con.commit()

def obter_jogo_por_usuario(con, id_usuario):
    query = "SELECT * FROM Jogo WHERE Usuario_idUsuario = %s"
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query, (id_usuario,))
        jogos = cursor.fetchall() #Retorna todos os resultados o Fetchone só retorna um
        
        return jogos
    
html_usuarios = obter_usuarios(con)
conexao_fechar(con)
