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

# def lista_favoritos(favoritos):
#     """Exibe a lista de favoritos do banco de dados como string"""
    
#     html_favoritos = ""  
#     for favorito in favoritos:
#         html_favoritos += (
#             f"ID Favorito: {favorito['idFavorito']} <br> "
#             f"ID Usuário: {favorito['idUsuario']} <br> "
#             f"ID Jogo: {favorito['idJogo']} <br> "
#             f"Data de Adição: {favorito['dataAdicao']} <br><br>"
#         )
        
#     return html_favoritos