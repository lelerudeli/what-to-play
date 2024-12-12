import mysql.connector

def conexao_abrir(config):
    """ Abre a conexão com o banco de dados usando as configurações do Flask. """
    return mysql.connector.connect(
        host=config['HOST'],
        user=config['USER'],
        password=config['PASSWORD'],
        database=config['NAME'],
        port=config['PORT']
    )

def conexao_fechar(con):
    """ Fecha a conexão com o banco de dados. """
    con.close()