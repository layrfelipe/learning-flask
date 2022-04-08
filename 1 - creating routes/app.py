from flask import Flask

app = Flask(__name__)

# 2 maneiras de criar rotas

# com decorator
@app.route("/")
def index():
    return "hello world"


# com metodo da lib -> add_url_rule(rule, endpoint, function)
def teste():
    return "<p>Testando</p>"

app.add_url_rule("/teste", "teste", teste)

if __name__ == '__main__':
    app.run()