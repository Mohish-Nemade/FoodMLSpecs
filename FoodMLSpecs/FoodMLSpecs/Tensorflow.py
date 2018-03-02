import subprocess, sys
import operator

def image_into_tensorflow(directory):
    p = subprocess.Popen( r'python $HOME/tensorflow/tensorflow/examples/label_image/label_image.py --graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt --input_layer=Mul --output_layer=final_result --input_mean=128 --input_std=128 --image=' + directory,shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    result=[]
    get=[]
    while True:
        out = p.stderr.read(1)
        print(out)
        get.append(p.stdout.read(1))
        res = "".join(get)
        if out == '' and p.poll() != None:
            break
        if out != '':
            result.append(out)
    print(res)
    res = res.split("\r")
    print(res)

    res = "".join(res).replace('\n',' ').split(" ")
    print(res)
    final_result = output_process(res)
    return final_result

def output_process(res):
    result = {}
    for i in range(0,len(res)-1,2) :
        if float(res[i+1]) > 0.80:
            result[res[i]] = float(res[i+1])
    for key in result:
        result[key] = {
            'calories': 10,
            'total-fat':25,
            'protein':30,
            'calcium':40,
        }
    print(result)
    return result

