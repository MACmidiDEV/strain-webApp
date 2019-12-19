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


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)

