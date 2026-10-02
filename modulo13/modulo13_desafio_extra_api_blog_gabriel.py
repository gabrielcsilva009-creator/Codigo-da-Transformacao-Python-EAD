from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

BANCO = "blog.db"


def conectar_banco():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabelas():
    conexao = conectar_banco()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    """)

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS Posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            usuario_id INTEGER NOT NULL
        )
    """)

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS Comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            post_id INTEGER NOT NULL,
            usuario_id INTEGER NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


# =========================
# AUTENTICAÇÃO
# =========================

@app.route("/cadastrar", methods=["POST"])
def cadastrar_usuario():
    dados = request.get_json()

    nome = dados.get("nome")
    senha = dados.get("senha")

    if not nome or not senha:
        return jsonify({
            "erro": "Nome e senha são obrigatórios."
        }), 400

    conexao = conectar_banco()

    conexao.execute("""
        INSERT INTO Usuarios (nome, senha)
        VALUES (?, ?)
    """, (nome, senha))

    conexao.commit()
    conexao.close()

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!"
    }), 201


@app.route("/login", methods=["POST"])
def login():
    dados = request.get_json()

    nome = dados.get("nome")
    senha = dados.get("senha")

    conexao = conectar_banco()

    usuario = conexao.execute("""
        SELECT * FROM Usuarios
        WHERE nome = ? AND senha = ?
    """, (nome, senha)).fetchone()

    conexao.close()

    if usuario is None:
        return jsonify({
            "erro": "Usuário ou senha incorretos."
        }), 401

    return jsonify({
        "mensagem": "Login realizado com sucesso!",
        "usuario_id": usuario["id"]
    })


# =========================
# POSTS
# =========================

@app.route("/posts", methods=["POST"])
def criar_post():
    dados = request.get_json()

    titulo = dados.get("titulo")
    conteudo = dados.get("conteudo")
    usuario_id = dados.get("usuario_id")

    if not titulo or not conteudo or not usuario_id:
        return jsonify({
            "erro": "Título, conteúdo e usuario_id são obrigatórios."
        }), 400

    conexao = conectar_banco()

    conexao.execute("""
        INSERT INTO Posts (titulo, conteudo, usuario_id)
        VALUES (?, ?, ?)
    """, (titulo, conteudo, usuario_id))

    conexao.commit()
    conexao.close()

    return jsonify({
        "mensagem": "Post criado com sucesso!"
    }), 201


@app.route("/posts", methods=["GET"])
def listar_posts():
    conexao = conectar_banco()

    posts = conexao.execute("""
        SELECT * FROM Posts
    """).fetchall()

    conexao.close()

    resultado = []

    for post in posts:
        resultado.append({
            "id": post["id"],
            "titulo": post["titulo"],
            "conteudo": post["conteudo"],
            "usuario_id": post["usuario_id"]
        })

    return jsonify(resultado)


# =========================
# COMENTÁRIOS
# =========================

@app.route("/comentarios", methods=["POST"])
def criar_comentario():
    dados = request.get_json()

    texto = dados.get("texto")
    post_id = dados.get("post_id")
    usuario_id = dados.get("usuario_id")

    if not texto or not post_id or not usuario_id:
        return jsonify({
            "erro": "Texto, post_id e usuario_id são obrigatórios."
        }), 400

    conexao = conectar_banco()

    conexao.execute("""
        INSERT INTO Comentarios (texto, post_id, usuario_id)
        VALUES (?, ?, ?)
    """, (texto, post_id, usuario_id))

    conexao.commit()
    conexao.close()

    return jsonify({
        "mensagem": "Comentário criado com sucesso!"
    }), 201


@app.route("/comentarios/<int:post_id>", methods=["GET"])
def listar_comentarios(post_id):
    conexao = conectar_banco()

    comentarios = conexao.execute("""
        SELECT * FROM Comentarios
        WHERE post_id = ?
    """, (post_id,)).fetchall()

    conexao.close()

    resultado = []

    for comentario in comentarios:
        resultado.append({
            "id": comentario["id"],
            "texto": comentario["texto"],
            "post_id": comentario["post_id"],
            "usuario_id": comentario["usuario_id"]
        })

    return jsonify(resultado)


if __name__ == "__main__":
    criar_tabelas()
    app.run(debug=True)