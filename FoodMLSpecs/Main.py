from flask import Flask,jsonify,request,abort
import DecodeImage
import Tensorflow
app = Flask(__name__)


result=[]


@app.route('/image/', methods=['POST'])
def upload_image():
    food_image = []
    print("sdsaasd")
    food_image = {
        'id': request.json['id'],
        'encoded_image': request.json['encoded_image'],
        'result_status': request.json.get('result_status'),
        'image_type': request.json.get('image_type'),
        #'food_name': request.json('food_image'),
       # 'food_details': request.json('food_details')
    }


    save_directory = DecodeImage.decode_image(food_image)
    food_output = Tensorflow.image_into_tensorflow(save_directory)
    food_image['food_name'] = food_output
    return jsonify({'food_image': food_image}), 201

if __name__ == '__main__':
    app.run(debug=True)


