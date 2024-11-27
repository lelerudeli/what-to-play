from app.conexao_banco import conexao_abrir, conexao_fechar

def listar_avaliacoes(app):
    """ Lista todas as avaliações do banco de dados. """
    config = app.config
    con = conexao_abrir(config)
    
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Avalia")
        avaliacoes = cursor.fetchall()
    
    conexao_fechar(con)  # Fecha a conexão
    return avaliacoes

# def lista_avaliacoes(avaliacoes):
#     """Exibe a lista de avaliações do banco de dados como string"""
    
#     html_avaliacoes = ""  
#     for avaliacao in avaliacoes:
#         html_avaliacoes += (
#             f"ID Avaliação: {avaliacao['idAvaliacao']} <br> "
#             f"ID Jogo: {avaliacao['idJogo']} <br> "
#             f"ID Usuário: {avaliacao['idUsuario']} <br> "
#             f"Avaliação: {avaliacao['avaliacao']} <br> "
#             f"Comentário: {avaliacao['comentario']} <br> "
#             f"Data de Avaliação: {avaliacao['dataAvaliacao']} <br><br>"
#         )
        
#     return html_avaliacoes