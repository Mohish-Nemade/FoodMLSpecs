from flask import Flask,jsonify,request,abort
import DecodeImage
import Tensorflow
app = Flask(__name__)


result=[]
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/tate/', methods=['GET'])
def get_tasks():
    return "hello tate"


@app.route('/image/', methods=['POST'])
def upload_image():
    food_image = []
    print("sdsaasd")
    food_image = {
        'id': request.json['id'],
        'encoded_image': request.json['encoded_image'],
        #'result_status': request.json('result_status'),
        'image_type': request.json.get('image_type'),
        #'food_name': request.json('food_image'),
       # 'food_details': request.json('food_details')
    }

    a=12
    result1 = {
        'id': 1,
        'title': a,
        'description': 1,
        'done': False
    }
    save_directory = DecodeImage.decode_image(food_image)
    Tensorflow.image_into_tensdorflow(save_directory)
    print("tatti")
   # print(result)
    print("tatti2")
   # print(result)
    #return jsonify({'food_image': food_image}),201
    return jsonify({'result1': result1}), 201

if __name__ == '__main__':
    app.run(debug=True)


