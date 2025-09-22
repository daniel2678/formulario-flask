import os
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/salvar", methods=["POST"])
def salvar():
    campo_a = request.form.get("campo_a", "").strip()
    campo_b = request.form.get("campo_b", "").strip()

    if campo_a and campo_b:
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write(f"{campo_a},{campo_b}\n")

    return redirect("/")

if __name__ == "__main__":
    # 🚨 use a porta do sistema, pois o Railway define automaticamente
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
