from flask import Flask, jsonify,request,abort
import DecodeImage
import Tensorflow
app = Flask(__name__)

food_image = []



@app.route('/image/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/image/', methods=['POST'])
def upload_image():
    if not request.json or not 'encode_image' in request.json:
        abort(400)


    food_image =   {
        'id': request.json['id'],
        'encoded_image': request.json['encoded_image'],
        'result_status': request.json('result_status'),
        'image_type': request.json('image_type'),
        'food_name': request.json('food_image'),
        'food_details': request.json('food_details')
    }

    save_directory = DecodeImage.decode_image(food_image)
    Tensorflow.image_into_tensdorflow(save_directory)


    tasks.append(task)
    return jsonify({'task': task})

def decode(des):
    getimage = base64.decodestring(des)
    i = Image.open(BytesIO(getimage))
    path = r'D:\tensorflow\abcd'
    i.save(path + '.jpg')


if __name__ == '__main__':
    app.run(debug=True)


