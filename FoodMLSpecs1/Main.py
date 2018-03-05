from flask import Flask,jsonify,request,abort,render_template
import Database,dbConnect,stringsearch
from werkzeug.utils import secure_filename
import DecodeImage
import Tensorflow
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='/home/ml/saveimage/'
app.config['upload_image']="/home/ml/saveimage/"

result=[]


@app.route('/upload/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET','POST'])
def upload_file1():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        #f.save(secure_filename(f.filename))
        f.save(os.path.join(app.config['upload_image'], f.filename))
        print(f.filename)
        return 'file uploaded successfully'

@app.route('/search/', methods=['POST'])
def search_image():
    userid = request.json['id']
    userin = request.json['user_input']
    db = dbConnect.connectDb()
    store = db.fooditem.find()
    result=[]
    for item in store:
        res = stringsearch.KMPSearch(userin,item["item"])
        if(res==1):
            result.append(item["item"])
        else:
            result.append("Not found")
    print(result)
    return jsonify(result)


@app.route('/image/', methods=['POST'])
def upload_image():
    food_image = []
    food_image = {
        'id': request.json['id'],
        'encoded_image': request.json['encoded_image'],
        'result_status': request.json.get('result_status'),
        'image_type': request.json.get('image_type'),
        'food_correct': request.json.get('food_correct'),
        'image_directory':request.json.get('image_directory'),
        #'food_name': request.json('food_image'),
       # 'food_details': request.json('food_details')
    }

    save_directory = DecodeImage.decode_image(food_image)
    food_image['image_directory'] = save_directory
    food_output = Tensorflow.image_into_tensorflow(save_directory)
    food_image['food_name'] = food_output
    #Database.insert_fun(food_image)

    return jsonify(food_image)



@app.route('/status/',methods=['POST'])
def status_image():
    food_image = {
        'id': request.json['id'],
        'encoded_image': request.json['encoded_image'],
        'result_status': request.json.get('result_status'),
        'image_type': request.json.get('image_type'),
        'image_directory':request.json.get('image_directory'),
        'food_correct': request.json.get('food_correct')
        #'food_name': request.json('food_image'),
       # 'food_details': request.json('food_details')
    }
    if food_image['result_status'] == 'True':
        dest_directory = "/home/ml/flower_photos/"+ food_image['food_correct'] + '/' + str(food_image['id']) + food_image['image_type']
        print(dest_directory)
        print(food_image['image_directory'])
        os.rename(food_image['image_directory'], dest_directory)
    else:
        #Search code to be written


        #if food not found in db
        if os.path.isdir("/home/ml/untrained/" + food_image['food_correct']):
            dest_directory = "/home/ml/untrained/" + food_image['food_correct'] + '/' + str(food_image['id']) + food_image['image_type']
            os.rename(food_image['image_directory'], dest_directory)
        else:
            directory = "/home/ml/untrained/" + food_image['food_correct']
            os.makedirs(directory)
            os.rename(food_image['image_directory'], directory + '/' + str(food_image['id']) + food_image['image_type'])



if __name__ == '__main__':
    app.run(debug=True)


