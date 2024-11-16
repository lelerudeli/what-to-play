from flask import Flask, render_template, request

# Definição de rotas aqui

app = Flask(__name__)

app.route('/')
def main ():
  return render_template('../frontend/src/index.html')


app.debug = True
# Definição de rotas com post ou get