import base64
from PIL import Image
from io import BytesIO


def decode_image(food_image):
    getimage = base64.decodestring(food_image['encoded_image'])
    i = Image.open(BytesIO(getimage))
    path = r'/home/ml/akshay/' + str(food_image['id'])
    i.save(path + food_image['image_type'])
    return path+food_image['image_type']