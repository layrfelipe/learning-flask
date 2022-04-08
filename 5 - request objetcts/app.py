from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # 2 formas de pegar os query params e passar pra dict
    
    # 1 forma
    dict1 = request.args.to_dict()

    # 2 forma
    dict2 = dict(request.args)

    return json.dumps(request.args) # query params - http://127.0.0.1:5000/?nome=layr&idade=22 

if __name__ == "__main__":
    app.run(debug=True)