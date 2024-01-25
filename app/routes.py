from app import routes
from flask import render_template, request, redirect, url_for
from app import app
from app import data
#from app.models import Todo
#from app import db
from random import randint as ri

@app.route('/')
def index():
    #incomplete = Todo.query.filter_by(complete=False).all()
    #complete = Todo.query.filter_by(complete=True).all()
    #return render_template('index.html', incomplete=incomplete, complete=complete)
    return render_template('index.html', incomplete=list(filter(lambda x : x['complete'] == False, data)), complete=list(filter(lambda x : x['complete'] == True, data)))

@app.route('/add', methods=['POST'])
def add():
    #todo = Todo(text=request.form['todoitem'], complete=False)
    data.append({'id': ri(1, 1000000), 'text': request.form['todoitem'], 'complete': False})

    #db.session.add(todo)
    #db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete(id):
    #todo = Todo.query.filter_by(id=int(id)).first()
    #todo.complete = True
    #db.session.commit()
    print(type(id))
    for el in data:
        if el['id'] == id:
            el['complete'] = True
            break

    return redirect(url_for('index'))