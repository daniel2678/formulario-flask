from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista para armazenar os dados em memória
dados_salvos = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        campo_a = request.form.get("campo_a")
        campo_b = request.form.get("campo_b")

        # Armazena os dados na lista
        dados_salvos.append({
            "campo_a": campo_a,
            "campo_b": campo_b
        })

        # Exibe nos logs (Railway verá isso!)
        print(f"[NOVO ENVIO] Campo A: {campo_a} | Campo B: {campo_b}")

        return "Dados recebidos com sucesso!"

    # Formulário simples
    return '''
        <form method="POST">
            Campo A: <input type="text" name="campo_a"><br>
            Campo B: <input type="text" name="campo_b"><br>
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
