from pymongo import MongoClient

import dbConnect



def insert_fun(food_image):
    db = dbConnect.connectDb()

'''collection = db.food_image.find()

    for x in collection:
        print("id=" + x["id"] + "encoded_image=" + x["encoded_image"]'''

    db.food_image.insert_one(food_image)

