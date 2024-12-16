from app.conexao_banco import conexao_abrir, conexao_fechar

def listar_favoritos(app):
    """ Lista todos os favoritos do banco de dados. """
    config = app.config
    con = conexao_abrir(config)
    
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Favorita")
        favoritos = cursor.fetchall()
    
    conexao_fechar(con)  # Fecha a conexão
    return favoritos

# idFavorito
# Usuario_idUsuario
# Jogo_idJogo
# dataFavorito
