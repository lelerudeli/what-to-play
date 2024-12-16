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
