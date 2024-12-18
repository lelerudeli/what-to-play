from app.conexao_banco import conexao_abrir, conexao_fechar
from datetime import datetime
import pytz
import bcrypt

# Define o fuso horário de Brasília
brasilia_tz = pytz.timezone('America/Sao_Paulo')

# Obtem a data e hora de brasília
data_atual = datetime.now(brasilia_tz)

# Formata a data
data_formatada = data_atual.strftime("%Y-%m-%d %H:%M:%S")

def criar_usuario(app, usuario_infos):
    """Insere um novo usuário no banco de dados."""
    config = app.config
    con = conexao_abrir(config)
    
    # Criptografa a senha
    senha = usuario_infos['senhaUsuario'].encode('utf-8')
    senha_criptografada = bcrypt.hashpw(senha, bcrypt.gensalt()) #Criptgrafa usando o bcrypt
    tipo_usuario = 'regular' #Pegar do sistema depois
    
    query = """
    INSERT INTO Usuario (dataRegistro,nomeUsuario, nomeCompleto, emailUsuario, tipoUsuario, senhaUsuario)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (
        data_formatada,
        usuario_infos['nomeUsuario'],
        usuario_infos['nomeCompleto'],
        usuario_infos['emailUsuario'],
        tipo_usuario,
        senha_criptografada.decode('utf-8') #Salva como string
    )
    
    with con.cursor() as cursor:
        cursor.execute(query, valores)
        con.commit()
    
    conexao_fechar(con)
    return cursor.lastrowid, tipo_usuario  # Retorna o ID do usuário

def autenticar_usuario(app, login_infos):
    """Autentica um usuário com base no e-mail e na senha."""
    config = app.config
    con = conexao_abrir(config)
    
    query = """
    SELECT nomeUsuario, idUsuario, senhaUsuario, tipoUsuario FROM Usuario WHERE emailUsuario = %s
    """
    valores = (login_infos['emailUsuario'],)  # Certifique-se de que é uma tupla
    
    try:
        with con.cursor() as cursor:
            cursor.execute(query, valores)
            resultado = cursor.fetchone()  # Busca uma linha correspondente
    except Exception as e:
        print(f"Erro na autenticação: {e}")
        return None, None, None
    finally:
        conexao_fechar(con)
    
    if resultado:
        nome_usuario, id_usuario, senha_armazenada, tipo_usuario = resultado

        senha = login_infos['senhaUsuario'].encode('utf-8')
        if bcrypt.checkpw(senha, senha_armazenada.encode('utf-8')):
            return nome_usuario, id_usuario, tipo_usuario
        
    return None, None, None

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


def verificar_email(app, email):
    """Verifica se o e-mail existe no banco de dados."""
    config = app.config
    con = conexao_abrir(config)

    query = """
    SELECT idUsuario, emailUsuario
    FROM Usuario
    WHERE emailUsuario = %s
    """
    valores = (email,)

    try:
        with con.cursor() as cursor:
            cursor.execute(query, valores)
            resultado = cursor.fetchone()  # Busca uma linha correspondente
    except Exception as e:
        print(f"Erro ao verificar e-mail: {e}")
        return None
    finally:
        conexao_fechar(con)

    if resultado:
        id_usuario, email_usuario = resultado
        return {"idUsuario": id_usuario, "emailUsuario": email_usuario}
    
    return None  # Retorna None se o e-mail não for encontrado

def obter_usuario_por_id(app, id_usuario):
    """Obtém os detalhes de um usuário usando o id, incluindo a contagem e lista de jogos."""
    config = app.config
    con = conexao_abrir(config)
    
    #Obter os dados do usuário
    query_usuario = "SELECT * FROM Usuario WHERE idUsuario = %s"
    
    with con.cursor(dictionary=True) as cursor:
        cursor.execute(query_usuario, (id_usuario,))
        usuario = cursor.fetchone() #Dados do usuário
    
    if usuario:
        usuario['dataRegistro'] = usuario['dataRegistro'].strftime('%Y-%m-%d %H:%M:%S')
        
        #Obter a lista de jogos do usuário
        query_jogos = "SELECT * FROM Jogo WHERE Usuario_idUsuario = %s"
        
        with con.cursor(dictionary=True) as cursor:
            cursor.execute(query_jogos, (id_usuario,))
            jogos = cursor.fetchall()  # Lista de jogos
        
        conexao_fechar(con)
        
        return {
            'id': usuario['idUsuario'],
            'nomeUsuario': usuario['nomeUsuario'],
            'nomeCompleto': usuario['nomeCompleto'],
            'emailUsuario': usuario['emailUsuario'],
            'tipoUsuario': usuario['tipoUsuario'],
            'dataRegistro': usuario['dataRegistro'],
            'quantidadeJogos': usuario['jogosUsuario'],  # Campo armazenado no banco
            'jogos': jogos  # Lista detalhada dos jogos
        }
    
    conexao_fechar(con)
    return None

def atualizar_usuario(app, id_usuario, usuario_infos):
    """Atualiza os dados de um usuário existente."""
    config = app.config
    con = conexao_abrir(config)
    
    query = """
    UPDATE Usuario
    SET nomeUsuario = %s, nomeCompleto = %s, emailUsuario = %s, tipoUsuario = %s
    WHERE idUsuario = %s
    """
    valores = (
        usuario_infos['nomeUsuario'],
        usuario_infos['nomeCompleto'],
        usuario_infos['emailUsuario'],
        usuario_infos['tipoUsuario'],
        id_usuario
    )
    
    with con.cursor() as cursor:
        cursor.execute(query, valores)
        con.commit()
    
    conexao_fechar(con)
    return cursor.rowcount  # Retorna o número de linhas atualizadas

def excluir_usuario(app, id_usuario):
    """Remove um usuário do banco de dados."""
    config = app.config
    con = conexao_abrir(config)
    
    query = "DELETE FROM Usuario WHERE idUsuario = %s"
    
    with con.cursor() as cursor:
        cursor.execute(query, (id_usuario,))
        con.commit()
    
    conexao_fechar(con)
    return cursor.rowcount  # Retorna o número de linhas atualizadas

