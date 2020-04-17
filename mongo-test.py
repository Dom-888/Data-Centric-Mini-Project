# Check if Atlas database is connected to the repo

import pymongo

import os

MONGODB_URI = 'mongodb+srv://RK3n:cimpalimpa089@cluster0-1hvju.mongodb.net/test?retryWrites=true&w=majority' 
DBS_NAME = "task_manager" 
COLLECTION_NAME = "tasks"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connect!")
        return conn
    except pymongo.error.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

# La variabile coll permette di manipolare il database usando i MongoDB metods: coll.method()
coll = conn[DBS_NAME][COLLECTION_NAME]

# Print the collection in the terminal
documents = coll.find()  
for doc in documents:
    print(doc)
	
