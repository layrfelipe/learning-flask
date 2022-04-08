from json import dumps
from flask import Flask, request

app = Flask(__name__, static_folder="public") # carregar html css e js

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        return f"<b>Usuário adicionado</b> <br/> {dumps(request.form)}" # request tem varios atributos para se trabalhar (forms, args etc) -> estudar mais sobre
    return "Ok (GET)"

if __name__ == "__main__":
    app.run(debug=True)