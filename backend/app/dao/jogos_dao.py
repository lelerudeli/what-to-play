from app.conexao_banco import conexao_abrir, conexao_fechar

def listar_jogos(app):
    """ Lista todos os jogos do banco de dados. """
    config = app.config
    con = conexao_abrir(config)
    
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Jogo")
        jogos = cursor.fetchall()
    
    conexao_fechar(con)  # Fecha a conexão
    return jogos

# #idJogo
# nomeJogo
# regraJogo
# tipoJogo (enum)
# faixaEtaria
# numeroCurtidas
# numeroJogadores
# Usuario_idUsuario
# ClassificacaoEtaria_idClassificacao
    
# def lista_jogos(jogos):
#     """Exibe a lista de jogos do banco de dados como string"""
    
#     html_jogos = ""  
#     for jogo in jogos:
#         html_jogos += (
#             f"ID Jogo: {jogo['idJogo']} <br> "
#             f"Nome do Jogo: {jogo['nomeJogo']} <br> "
#             f"Tipo de Jogo: {jogo['tipoJogo']} <br> "
#             f"Faixa Etária: {jogo['faixaEtaria']} <br> "
#             f"Número de Curtidas: {jogo['numCurtidas']} <br> "
#             f"Número de Jogadores: {jogo['numJogadores']} <br> "
#             f"Data de Lançamento: {jogo['dataLancamento']} <br> "
#             f"Gênero: {jogo['generoJogo']} <br> "
#             f"Plataforma: {jogo['plataformaJogo']} <br><br>"
#         )
        
#     return html_jogos