from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

BANCO = "usuarios.db"


def conectar_banco():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({
            "erro": "Nome e email são obrigatórios."
        }), 400

    conexao = conectar_banco()

    conexao.execute("""
        INSERT INTO Usuarios (nome, email)
        VALUES (?, ?)
    """, (nome, email))

    conexao.commit()
    conexao.close()

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!"
    }), 201


@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    conexao = conectar_banco()

    usuarios = conexao.execute("""
        SELECT * FROM Usuarios
    """).fetchall()

    conexao.close()

    resultado = []

    for usuario in usuarios:
        resultado.append({
            "id": usuario["id"],
            "nome": usuario["nome"],
            "email": usuario["email"]
        })

    return jsonify(resultado)


if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)