from whattoplay.application.func.conexao_bd import conexao_abrir, conexao_fechar
from bcrypt import checkpw

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
        
def autenticar_usuario(con, login_infos):
    """Autentica um usuário com base no e-mail e na senha."""
    
    query = """
    SELECT idUsuario, senhaUsuario
    FROM Usuario
    WHERE emailUsuario = %s
    """
    valores = (login_infos['email'],)  # Certifique-se de que é uma tupla
    
    try:
        with con.cursor() as cursor:
            cursor.execute(query, valores)
            resultado = cursor.fetchone()  # Busca uma linha correspondente
    except Exception as e:
        print(f"Erro na autenticação: {e}")
        return None
    finally:
        conexao_fechar(con)
    
    if resultado:
        id_usuario, senha_armazenada = resultado
        # Verifica se a senha fornecida corresponde ao hash armazenado
        if resultado and senha_armazenada:
            if checkpw(login_infos['senha'].encode('utf-8'), senha_armazenada.encode('utf-8')):
                return id_usuario
        
    return None

def verificar_email(con, email):
    query = "SELECT idUsuario, emailUsuario FROM Usuario WHERE emailUsuario = %s"
    valores = (email,)
    try:
        with con.cursor() as cursor:
            cursor.execute(query, valores)
            resultado = cursor.fetchone()
    except Exception as e:
        print(f"Erro ao verificar e-mail: {e}")
        return None
    if resultado:
        id_usuario, email_usuario = resultado
        return {"idUsuario": id_usuario, "emailUsuario": email_usuario}
    return None
        

def excluir_usuario(con, id_usuario):
    """Remove um usuário do banco de dados."""
    query = "DELETE FROM Usuario WHERE idUsuario = %s"
    
    with con.cursor() as cursor:
        cursor.execute(query, (id_usuario,))
        con.commit()

def obter_jogo_por_id(con, id_jogo):
    query = "SELECT * FROM Jogo WHERE idJogo = %s"
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query, (id_jogo,))
        return cursor.fetchone()
    
def obter_jogo_por_tipo(con, tipo_jogo):
    query = "SELECT * FROM Jogo WHERE tipoJogo = %s"
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query, (tipo_jogo,))
        return cursor.fetchall()

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
