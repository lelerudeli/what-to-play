from app.conexao_banco import conexao_abrir, conexao_fechar

def listar_classificacoes_etarias(app):
    """ Lista todas as classificações etárias do banco de dados. """
    config = app.config
    con = conexao_abrir(config)
    
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM ClassificacaoEtaria")
        classificacoes_etarias = cursor.fetchall()
    
    conexao_fechar(con)  # Fecha a conexão
    return classificacoes_etarias

# idClassificacao
# sexo
# bebida
# entorpecentes
# psicossomaticos
# linguagemImpropria
# violencia
# classificacao

# def lista_classificacoes_etarias(classificacoes_etarias):
#     """Exibe a lista de classificações etárias do banco de dados como string"""
    
#     html_classificacoes_etarias = ""  
#     for classificacao in classificacoes_etarias:
#         html_classificacoes_etarias += (
#             f"ID Classificação: {classificacao['idClassificacao']} <br> "
#             f"Faixa Etária: {classificacao['faixaEtaria']} <br> "
#             f"Descrição: {classificacao['descricao']} <br><br>"
#         )
        
#     return html_classificacoes_etarias