from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def inicio():
    return jsonify({"mensagem": "API funcionando!"})


@app.route("/soma/<int:a>/<int:b>")
def soma(a, b):
    return jsonify({"resultado": a + b})


if __name__ == "__main__":
    app.run(debug=True)