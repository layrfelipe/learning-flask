from datetime import datetime
from email.mime import application
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simple_crud.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        return {"id": self.id, "username": self.username, "email": self.email}


def handleResponse(status, content_name, content, message=False):
    body = {}

    body[content_name] = content

    if (message):
        body["message"] = message

    return Response(json.dumps(body), status=status, mimetype="application/json")


@app.route("/users", methods=["GET"])
def select_all():
    users_objects = User.query.all()

    users_json = [user.to_json() for user in users_objects]
    
    return handleResponse(200, "users", users_json)


@app.route("/user/<id>", methods=["GET"])
def select_user(id):
    user_object = User.query.filter_by(id=id).first()
    user_json = user_object.to_json()

    return handleResponse(200, "user", user_json)


@app.route("/user", methods=["POST"])
def add_user():
    body = request.get_json()

    try:
        user = User(username=body["username"], email=body["email"])
        db.session.add(user)
        db.session.commit()

        return handleResponse(201, "user", user.to_json(), "User created")
    except Exception as e:
        print(e)
        return handleResponse(400, "user", {}, "Error")


@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
    user_object = User.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if "username" in body:
            user_object.username = body["username"]
        if "email" in body:
            user_object.email = body["email"]

        db.session.add(user_object)
        db.session.commit()

        return handleResponse(200, "user", user_object.to_json(), "User updated")
    except Exception as e:
        print(e)
        return handleResponse(400, "user", {}, "Error")


@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    user_object = User.query.filter_by(id=id).first()
    
    try:
        db.session.delete(user_object)
        db.session.commit()

        return handleResponse(200, "user", user_object.to_json(), "User deleted")
    except Exception as e:
        print(e)
        return handleResponse(400, "user", {}, "Error")



app.run()