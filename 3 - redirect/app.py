from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/admin")
def admin():
    return "<h1>Admin</h1>"

@app.route("/guest/<guest_name>")
def guest(guest_name):
    return f'Hello, guest <b>{guest_name}</b>'

@app.route("/user/<name>")
def user(name):
    if name=="admin":
        return redirect(url_for("admin")) # tambem da pra botar http://127.0.0.1:5000/admin MAS URL_FOR EH MELHOR
    else:
        return redirect(url_for("guest", guest_name=name))

if __name__ == "__main__":
    app.run(debug=True)