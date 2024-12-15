from app.conexao_banco import conexao_abrir, conexao_fechar

def obter_jogos(app):
    config = app.config
    con = conexao_abrir(config)
    
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Jogo")
        jogos = cursor.fetchall()
        
    conexao_fechar(con)
    return jogos

def obter_jogo_por_tipo(app, tipo_jogo):
    config = app.config
    con = conexao_abrir(config)
    
    query = "SELECT * FROM Jogo WHERE tipoJogo = %s"
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query, (tipo_jogo,))
        jogos = cursor.fetchone()
    
    conexao_fechar(con)
    return jogos

def obter_jogo_por_id(app, id_jogo):
    config = app.config
    con = conexao_abrir(config)
    
    query = "SELECT * FROM Jogo WHERE idJogo = %s"
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query, (id_jogo,))
        jogo = cursor.fetchone()
    
    conexao_fechar(con)
    return jogo

def criar_jogo(app, jogo_infos):
    config = app.config
    con = conexao_abrir(config)
    
    query = """
    INSERT INTO Jogo (
        nomeJogo, regraJogo, tipoJogo, faixaEtaria, 
        numeroCurtidas, numeroJogadores, 
        Usuario_idUsuario, ClassificacaoEtaria_idClassificacao
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        jogo_infos['nomeJogo'],
        jogo_infos['regraJogo'],
        jogo_infos['tipoJogo'],
        jogo_infos['faixaEtaria'],
        jogo_infos['numeroCurtidas'],
        jogo_infos['numeroJogadores'],
        jogo_infos['Usuario_idUsuario'],
        jogo_infos['ClassificacaoEtaria_idClassificacao']
    )
    with con.cursor() as cursor:
        cursor.execute(query, valores)
        con.commit()
    jogo = cursor.lastrowid
    conexao_fechar(con)
    return jogo

def atualizar_jogo(app, id_jogo, jogo_infos):
    config = app.config
    con = conexao_abrir(config)
    
    query = """
    UPDATE Jogo
    SET nomeJogo = %s, regraJogo = %s, tipoJogo = %s, faixaEtaria = %s, 
        numeroCurtidas = %s, numeroJogadores = %s, 
        Usuario_idUsuario = %s, ClassificacaoEtaria_idClassificacao = %s
    WHERE idJogo = %s
    """
    valores = (
        jogo_infos['nomeJogo'],
        jogo_infos['regraJogo'],
        jogo_infos['tipoJogo'],
        jogo_infos['faixaEtaria'],
        jogo_infos['numeroCurtidas'],
        jogo_infos['numeroJogadores'],
        jogo_infos['Usuario_idUsuario'],
        jogo_infos['ClassificacaoEtaria_idClassificacao'],
        id_jogo
    )
    with con.cursor() as cursor:
        cursor.execute(query, valores)
        con.commit()
        
    conexao_fechar(con)
    return cursor.rowcount

def excluir_jogo(app, id_jogo):
    config = app.config
    con = conexao_abrir(config)
    
    query = "DELETE FROM Jogo WHERE idJogo = %s"
    with con.cursor() as cursor:
        cursor.execute(query, (id_jogo,))
        con.commit()
        
    conexao_fechar(con)
    return cursor.rowcount

def obter_jogo_por_usuario(app, id_usuario):
    config = app.config
    con = conexao_abrir(config)
    
    query = "SELECT * FROM Jogo WHERE Usuario_idUsuario = %s"
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query, (id_usuario,))
        jogos = cursor.fetchall() #Retorna todos os resultados o Fetchone só retorna um
        
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