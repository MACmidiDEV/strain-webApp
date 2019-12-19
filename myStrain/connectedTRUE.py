import pymongo
import os


MONGODB_URI = "mongodb+srv://root:r00tUser@strainapicluster-euclv.mongodb.net/strainAPI?retryWrites=true&w=majority"
DBS_NAME = "strainAPI"
COLLECTION_NAME = "strains"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)