from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome or not email:
        return jsonify({
            "erro": "Nome e email são obrigatórios."
        }), 400

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!",
        "nome": nome,
        "email": email
    }), 201


if __name__ == "__main__":
    app.run(debug=True)