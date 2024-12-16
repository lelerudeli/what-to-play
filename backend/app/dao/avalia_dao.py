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

# idAvaliacao
# dataAvaliacao
# Jogo_idJogo
# Usuario_idUsuario
