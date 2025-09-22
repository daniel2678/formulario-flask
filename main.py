from flask import Flask, request, jsonify

app = Flask(__name__)
dados_salvos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        campo_a = request.form.get("campo_a")
        campo_b = request.form.get("campo_b")
        dados_salvos.append({"campo_a": campo_a, "campo_b": campo_b})
        print(f"Novo dado: {campo_a}, {campo_b}")
        return "Dados recebidos com sucesso!"
    
    return '''
        <form method="POST">
            Campo A: <input name="campo_a"><br>
            Campo B: <input name="campo_b"><br>
            <input type="submit" value="Enviar">
        </form>
    '''

@app.route("/dados", methods=["GET"])
def listar_dados():
    return jsonify(dados_salvos)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
