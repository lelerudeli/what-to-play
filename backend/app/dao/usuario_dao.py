from app.conexao_banco import conexao_abrir, conexao_fechar

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

def criar_usuario(app, usuario_infos):
    """Insere um novo usuário no banco de dados."""
    config = app.config
    con = conexao_abrir(config)
    
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
    
    conexao_fechar(con)
    return cursor.lastrowid  # Retorna o ID do usuário 

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

