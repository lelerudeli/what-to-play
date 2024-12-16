from app.conexao_banco import conexao_abrir, conexao_fechar

def criar_usuario(app, usuario_infos):
    """Insere um novo usuário no banco de dados."""
    config = app.config
    con = conexao_abrir(config)
    
    query = """
    INSERT INTO Usuario (nomeUsuario, nomeCompleto, emailUsuario, tipoUsuario, senhaUsuario)
    VALUES (%s, %s, %s, %s, %s)
    """
    valores = (
        usuario_infos['nomeUsuario'],
        usuario_infos['nomeCompleto'],
        usuario_infos['emailUsuario'],
        'regular',
        usuario_infos['senhaUsuario']
    )
    
    with con.cursor() as cursor:
        cursor.execute(query, valores)
        con.commit()
    
    conexao_fechar(con)
    return cursor.lastrowid  # Retorna o ID do usuário

def autenticar_usuario(app, login_infos):
    """Autentica um usuário com base no e-mail e na senha."""
    config = app.config
    con = conexao_abrir(config)
    
    query = """
    SELECT idUsuario, senhaUsuario, tipoUsuario FROM Usuario WHERE emailUsuario = %s
    """
    valores = (login_infos['emailUsuario'],)  # Certifique-se de que é uma tupla
    
    try:
        with con.cursor() as cursor:
            cursor.execute(query, valores)
            resultado = cursor.fetchone()  # Busca uma linha correspondente
    except Exception as e:
        print(f"Erro na autenticação: {e}")
        return None, None
    finally:
        conexao_fechar(con)
    
    if resultado:
        id_usuario, senha_armazenada, tipo_usuario = resultado
        # Verifica se a senha fornecida corresponde ao valor armazenado
        if login_infos['senhaUsuario'] == senha_armazenada:  # Comparação direta
            return id_usuario, tipo_usuario
        
    return None, None

def listar_usuarios(app):
    """ Lista todos os usuários do banco de dados. """
    # Obtenha as configurações diretamente da app.config
    config = app.config
    con = conexao_abrir(config)
    
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Usuario")
        usuarios = cursor.fetchall()
    
    conexao_fechar(con)  # Fecha a conexão
    return usuarios


def verificar_email(app, email):
    """Verifica se o e-mail existe no banco de dados."""
    config = app.config
    con = conexao_abrir(config)

    query = """
    SELECT idUsuario, emailUsuario
    FROM Usuario
    WHERE emailUsuario = %s
    """
    valores = (email,)

    try:
        with con.cursor() as cursor:
            cursor.execute(query, valores)
            resultado = cursor.fetchone()  # Busca uma linha correspondente
    except Exception as e:
        print(f"Erro ao verificar e-mail: {e}")
        return None
    finally:
        conexao_fechar(con)

    if resultado:
        id_usuario, email_usuario = resultado
        return {"idUsuario": id_usuario, "emailUsuario": email_usuario}
    
    return None  # Retorna None se o e-mail não for encontrado

def obter_usuario_por_id(app, id_usuario):
    """Obtém os detalhes de um usuário usando o id."""
    config = app.config
    con = conexao_abrir(config)
    
    query = "SELECT * FROM Usuario WHERE idUsuario = %s"
    
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query, (id_usuario,))
        usuario = cursor.fetchone()
    
    conexao_fechar(con)
    return usuario

def atualizar_usuario(app, id_usuario, usuario_infos):
    """Atualiza os dados de um usuário existente."""
    config = app.config
    con = conexao_abrir(config)
    
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
    
    conexao_fechar(con)
    return cursor.rowcount  # Retorna o número de linhas atualizadas

def excluir_usuario(app, id_usuario):
    """Remove um usuário do banco de dados."""
    config = app.config
    con = conexao_abrir(config)
    
    query = "DELETE FROM Usuario WHERE idUsuario = %s"
    
    with con.cursor() as cursor:
        cursor.execute(query, (id_usuario,))
        con.commit()
    
    conexao_fechar(con)
    return cursor.rowcount  # Retorna o número de linhas atualizadas

