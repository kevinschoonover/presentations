from flask import Flask, request
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST', 'PATCH', 'DELETE'])
def hello():
    if request.method == 'GET':
        return 'GET Request'
    elif request.method == 'POST':
        return 'POST Request'
    elif request.method == 'PATCH':
        return 'PATCH Request'
    elif request.method == 'DELETE':
        return 'DELETE Request'
    else:
        return 'Request'
