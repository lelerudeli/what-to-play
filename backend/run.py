from app import iniciar_app
from app.conexao_banco import conexao_abrir, conexao_fechar

app = iniciar_app()

if __name__ == "__main__":
    app.run(debug=True)
