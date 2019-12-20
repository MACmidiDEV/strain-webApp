import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'strainAPI'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@strainapicluster-euclv.mongodb.net/strainAPI?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_strains')
def get_strains():
    return render_template("strains.html", strains=mongo.db.strains.find())

@app.route('/add_strain')
def add_strain():    
    return render_template('addstrain.html', strains=mongo.db.strains.find())   

@app.route('/insert_strain', methods=['POST'])
def insert_strain():
    strains = mongo.db.strains
    strains.insert_one(request.form.to_dict())
    return redirect(url_for('get_strains'))     

@app.route('/edit_strain/<strain_id>')
def edit_strain(strain_id):
    the_strain = mongo.db.strains.find_one({"_id": ObjectId(strain_id)})
    # all_types = mongo.db.strains.find()
    all_types = mongo.db.type.find()
    return render_template('editstrain.html', strain=the_strain, type=all_types)

@app.route('/DB')
def get_DB():
    return render_template("DB-all.html", strains=mongo.db.strains.find())

@app.route('/add_DB')
def add_DB():    
    return render_template('DB-add.html', strains=mongo.db.strains.find())    

@app.route('/insert_DB', methods=['POST'])
def insert_DB():
    strains = mongo.db.strains
    strains.insert_one(request.form.to_dict())
    return redirect(url_for('get_DB'))

@app.route('/edit_DB/<strain_id>')
def edit_DB(strain_id):
    db_strain = mongo.db.strains.find_one({"_id": ObjectId(strain_id)})
    db_types = mongo.db.type.find()
    type_list = [typeX for typeX in db_types]
    return render_template('DB-edit.html', strain=db_strain , type=type_list)

@app.route('/update_DB/<strain_id>', methods=["POST"])
def update_DB(strain_id):
    strains = mongo.db.strains
    strains.update( {'_id': ObjectId(strain_id)},
    {
        'strain_name':request.form.get('name'),
        'strain_type':request.form.get('type'),
        'strain_description': request.form.get('description'),
        'firstTried': request.form.get('firstTried'),
        'isDank':request.form.get('isDank')
    })
    return redirect(url_for('get_DB'))    

      
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

