import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"
    ] = 'strainAPI'
app.config["MONGO_URI"
    ] = "mongodb+srv://root:r00tUser@strainapicluster-euclv.mongodb.net/strainAPI?retryWrites=true&w=majority"

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
    all_types = mongo.db.type.find()
    return render_template('editstrain.html', strain=the_strain, type=all_types)

@app.route('/update_strain/<strain_id>', methods=["POST"])
def update_strain(strain_id):
    strains = mongo.db.strains
    strains.update( {'_id': ObjectId(strain_id)},
    {
        'name':request.form.get('name'),
        'type':request.form.get('type'),
        'effects':request.form.get('effects'),
        'medical':request.form.get('medical'),
        'description': request.form.get('description'),
        'firstTried': request.form.get('firstTried'),
        'isDank':request.form.get('isDank'),
        'rankfire':request.form.get('rankfire')
    })
    return redirect(url_for('get_strains'))       

@app.route('/delete_strain/<strain_id>')
def delete_strain(strain_id):
    mongo.db.strains.delete_one({'_id': ObjectId(strain_id)})
    return redirect(url_for('get_strains'))        

@app.route('/get_ranks')
def get_ranks():
    return render_template("ranks.html", rankfire=mongo.db.rankfire.find()) 

@app.route('/edit_rank/<strain_id>')
def edit_rank(strain_id):
    return render_template('editstrain.html',
                           strain=mongo.db.rankfire.find_one(
                           {'_id': ObjectId(strain_id)}))


@app.route('/update_rank/<strain_id>', methods=['POST'])
def update_rank(strain_id):
    mongo.db.rankfire.update(
        {'_id': ObjectId(strain_id)},
        {'rankfire': request.form.get('rankfire')})
    return redirect(url_for('get_ranks'))    




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
        'name':request.form.get('name'),
        'type':request.form.get('type'),
        'effects':request.form.get('effects'),
        'medical':request.form.get('medical'),
        'description': request.form.get('description'),
        'firstTried': request.form.get('firstTried'),
        'isDank':request.form.get('isDank'),
        'rankfire':request.form.get('rankfire')
    })
    return redirect(url_for('get_DB'))    

@app.route('/delete_DB/<strain_id>')
def delete_DB(strain_id):
    mongo.db.strains.remove({'_id': ObjectId(strain_id)})
    return redirect(url_for('get_DB'))    

@app.route('/RanksDB')
def RanksDB():
    return render_template('RanksDB.html',
                           rankfire=mongo.db.fire.find())   

@app.route('/edit_RanksDB/<rankfire_id>')
def edit_RanksDB(rankfire_id):
    return render_template('EditRanksDB.html',
                           rankfire=mongo.db.rankfire.find_one(
                           {'_id': ObjectId(rankfire_id)}))      


@app.route('/update_RanksDB/<rankfire_id>', methods=['POST'])
def update_RanksDB(rankfire_id):
    mongo.db.rankfire.update(
        {'_id': ObjectId(rankfire_id)},
        {'rankfire': request.form.get('rankfire_fire')})
    return redirect(url_for('RanksDB'))  
      
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

