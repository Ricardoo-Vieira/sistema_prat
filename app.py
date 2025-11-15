from flask import Flask, render_template, request, redirect
from models import GerenciadorTarefas

app = Flask(__name__)
gerenciador = GerenciadorTarefas()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        titulo = request.form["titulo"]
        gerenciador.adicionar_tarefa(titulo)
        return redirect("/")

    tarefas = gerenciador.listar_tarefas()
    return render_template("index.html", tarefas=tarefas)

if __name__ == "__main__":
    app.run(debug=True)
