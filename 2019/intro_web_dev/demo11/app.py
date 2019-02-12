from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

todos = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('todo.html', todos=todos)
    else:
        todos.append(request.form['task'])
        return redirect("/")


@app.route('/todos/<int:id>/', methods=['GET'])
def delete_todo(id):
    """
    WARNING: Do NOT do this in production. This is simply a demostration of
    using completely backend based rendering (HTML Forms do NOT allow DELETE
    requests). You should use DELETE requests when deleting items on the
    backend.
    """
    todos.pop(id)
    return redirect("/")
