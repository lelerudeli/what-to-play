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


def lista_usuarios(usuarios):
    """Exibe a lista de usuários do banco de dados como string"""
    
    html_usuarios = ""  
    for usuario in usuarios:
        html_usuarios += (
            f"Usuario: {usuario['idUsuario']} <br> "
            f"Nome: {usuario['nomeUsuario']} <br> "
            f"Nome completo: {usuario['nomeCompleto']} <br> "
            f"Jogos do usuário: {usuario['jogosUsuario']} <br> "
            f"Data de Registro: {usuario['dataRegistro']} <br> "
            f"Email: {usuario['emailUsuario']} <br> "
            f"Tipo Usuário: {usuario['tipoUsuario']} <br><br>"
        )
        
    return html_usuarios
