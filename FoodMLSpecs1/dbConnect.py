from pymongo import MongoClient



def connectDb():
    client = MongoClient('localhost:27017')
    db = client.image
    return db
