from flask import Flask

app = Flask(__name__)

# se a rota for so hello, nao quebra
@app.route("/hello/")
@app.route("/hello/<name>") # route params dentro de <>
def hello(name=""):
    return f'<h1>Hello {name}</h1>'

@app.route("/blog/")
@app.route("/blog/<int:postID>") # da pra definir a tipagem para evitar erros
def blog(postID=-1):
    if postID >= 0:
        return f'blog info: {postID}'
    else:
        return f'this is home'

if __name__ == '__main__':
    app.run(debug=True)