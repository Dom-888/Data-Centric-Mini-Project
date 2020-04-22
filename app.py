import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId # Necessario alla funzione edit_task

# Collega il database al repo
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
# Substitute with an enviroment variable
app.config["MONGO_URI"] = 'mongodb+srv://RK3n:cimpalimpa089@cluster0-1hvju.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())


@app.route('/add_task')
def add_task():
    return render_template('addtask.html',
    categories=mongo.db.categories.find())  # La variabile categories contiene i risultati della query categories.find(). E' possibile estrarli con un for loop

# Attiva l'add task button 
@app.route('/insert_task', methods=['POST']) # Insert task va inserito nel form tag con jinja
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))

# Attiva l'edit button
@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task = mongo.db.task.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edittask.html', task=the_task, categories=all_categories)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
