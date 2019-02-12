from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('todo.html')
