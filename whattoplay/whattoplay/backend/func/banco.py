from whattoplay.backend.func.conexao_bd import conexao_abrir, conexao_fechar

# Abrir a conexão
con = conexao_abrir("junction.proxy.rlwy.net", "root", "uXoouZATPTMRXWqFnlUJgRxHozhruwzx", "whattoplay", 59391)

def listar_usuarios(con):
    with con.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM Usuario")
        usuarios = cursor.fetchall() 
        
        # Acumula os resultados em uma string
        resultado = ""
        for usuario in usuarios:
            resultado += (
                f"Usuario: {usuario['idUsuario']} <br> "
                f"Nome: {usuario['nomeUsuario']} <br> "
                f"Nome completo: {usuario['nomeCompleto']} <br> "
                f"Jogos do usuário: {usuario['jogosUsuario']} <br> "
                f"Data de Registro: {usuario['dataRegistro']} <br> "
                f"Email: {usuario['emailUsuario']} <br> "
                f"Tipo Usuário: {usuario['tipoUsuario']} <br><br>"
            )
        
        return resultado

html_usuarios = listar_usuarios(con)
print(html_usuarios)
conexao_fechar(con)
