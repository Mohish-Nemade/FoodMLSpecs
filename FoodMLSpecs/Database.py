from pymongo import MongoClient

import dbConnect



def insert_fun(food_image):
    db = dbConnect.connectDb()



    db.food_image.insert_one(food_image)




