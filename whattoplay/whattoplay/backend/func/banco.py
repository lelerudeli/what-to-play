from whattoplay.backend.func.conexao_bd import conexao_abrir,conexao_fechar

con = conexao_abrir("junction.proxy.rlwy.net", "root", "uXoouZATPTMRXWqFnlUJgRxHozhruwzx", "whattoplay", 59391)
def listar_usuarios(con):
    cursor = con.cursor(dictionary=True)  # Criar o cursor com a opção de retorno como dicionário
    sqlcode = "SELECT * FROM Usuario"
    cursor.execute(sqlcode)

    for usuario in cursor:
        return(f"Usuario: {usuario['idUSuario']} Nome: {usuario['nomeUSuario']} Nome completo: {usuario['nomeCompleto']} Jogos do usuário: {usuario['jogosUsuario']} dataRegistro {usuario['dataRegistro']}Email: {usuario['emailUsuario']} Tipo Usuário {usuario['tipoUsuario']}")

    cursor.close()
    con.commit()

listar_usuarios(con)

conexao_fechar(con)

