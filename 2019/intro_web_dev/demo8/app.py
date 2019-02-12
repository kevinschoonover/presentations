from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    return "/users/<br />/posts/<br />/folders/"


@app.route("/users/<username>/")
def user(username):
    return "User {}".format(username)


@app.route("/posts/<int:id>/")
def post(id):
    return "Post #{}".format(id)


@app.route("/folders/<path:subpath>/")
def folder(subpath):
    return "Folder is {}".format(subpath)
