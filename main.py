from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
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
