from flask import Flask, render_template, request
from whattoplay.backend.func.banco import listar_usuarios, con

# Definição de rotas aqui

app = Flask(__name__)

@app.route('/')
def main ():
  return listar_usuarios(con)

if __name__=='__main__':
  app.run(debug=True)
# Definição de rotas com post ou get