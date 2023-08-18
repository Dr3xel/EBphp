# Import Required Modules
from flask import Flask, render_template, request, redirect, url_for

#Create an Instance of Flask
app = Flask(__name__, template_folder='templates')

# Initialize Todo List
todos = [{'task': 'Sample task', 'done': False}]

#Define Route for the Homepage
@app.route('/')
def index():
    return render_template('index.html', todos=todos)

# add task
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('todo')
    todos.append({'task': task, 'done': False})
    return redirect('/')

#edit task
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        new_task = request.form.get('todo')
        todos[index]['task'] = new_task
        return redirect('/')
    return render_template('edit.html', todo=todos[index], index=index)

# check/uncheck task
@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect('/')

# delete task
@app.route('/delete/<int:index>')
def delete(index):
    todos.pop(index)
    return redirect('/')

# run the application
if __name__ == '__main__':
    app.run(debug=True)