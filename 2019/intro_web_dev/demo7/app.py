from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    return "You've found the index page."


@app.route("/secret/")
def hidden():
    return (
        "Welcome to Equifax's Management Page.<br />Your SSN is 123-45-6789."
    )
