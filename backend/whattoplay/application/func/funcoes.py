from flask import request,session,redirect,url_for

def login_func(users):
   usuarios = users
   if request.method == 'POST':
        nome_usuario = request.form['nomeUsuario']
        senha = request.form['senhaUsuario']
        
        usuario = next((user for user in usuarios if user['nomeUsuario'] == nome_usuario and user['senhaUsuario'] == senha), None)
        if usuario:
            session['usuario_logado'] = usuario['idUsuario']
            return redirect(url_for('api'))
        else:
            return "Usuário ou senha inválidos."
