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
    recipes=mongo.db.recipes.find(),
    preparation=mongo.db.preparation_time.find(),
    serv=mongo.db.serves.find(),
    diff=mongo.db.difficulty.find())

@app.route('/', methods=['POST', 'GET'])
@app.route('/show_recipes', methods=['POST', 'GET'])
def filter_recipes():
    filter_by = []
    filter = request.form
    for key in filter: 
        value_key = key
        filter_by.append({value_key: request.form[value_key]})
        filtered = mongo.db.recipes.find({'$and':filter_by})
    return render_template("recipes.html", filt = filtered, preparation=mongo.db.preparation_time.find(),serv=mongo.db.serves.find(),diff=mongo.db.difficulty.find())

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

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipes=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    preparation=mongo.db.preparation_time.find()
    serv=mongo.db.serves.find()
    diff=mongo.db.difficulty.find()
    return render_template("editrecipe.html", recipe=recipes, prep=preparation, ser=serv, dif=diff)
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'preparation_time':request.form.get('preparation_time'),
        'serves': request.form.get('serves'),
        'difficulty': request.form.get('difficulty'),
        'ingredients':request.form.get('ingredients'),
        'step_1':request.form.get('step_1'),
        'step_2':request.form.get('step_2'),
        'step_3':request.form.get('step_3'),
        'step_4':request.form.get('step_4'),
        'step_5':request.form.get('step_5'),
        'step_6':request.form.get('step_6')
    })
    return redirect(url_for('show_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('show_recipes'))
        
        
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug='True')