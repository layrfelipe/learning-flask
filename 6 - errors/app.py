from os import abort
from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__, static_folder="public")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (request.form["username"] == "admin" and request.form["pass"] == "admin"):
            return redirect(url_for("sucess"), code=302)
        else:
            abort(401)
    else:
        abort(403)

@app.route("/sucess")
def sucess ():
    return "sucess"

if __name__ == "__main__":
    app.run(debug=True)