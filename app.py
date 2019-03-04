import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = 'mongodb://jonw83:200JnFsWs183@ds343985.mlab.com:43985/cookbook'

mongo = PyMongo(app)

@app.route('/')
@app.route('/show_recipes')
def show_recipes():
    return render_template("recipes.html",
    recipes=mongo.db.recipes.find())

@app.route('/add_recipes')
def add_recipes():
    return render_template('addrecipes.html',
    preparation=mongo.db.preparation_time.find(),
    serv=mongo.db.serves.find(),
    diff=mongo.db.difficulty.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('show_recipes'))
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug='True')