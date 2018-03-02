import subprocess, sys

def image_into_tensdorflow(directory):
    print('dfsfdf')
    p = subprocess.Popen( r'python D:\tensorflow\tensorflow-master\tensorflow-master\tensorflow\examples\label_image\label_image.py --graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt --input_layer=Mul --output_layer=final_result --input_mean=128 --input_std=128 --image=D:\tensorflow\tensorflow-master\tensorflow-master\tensorflow\examples\label_image\flower_photos\daisy\21652746_cc379e0eea_m.jpg',shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    print("dddsas")
    result=[]
    get=[]
    while True:
        out = p.stderr.read(1)
        get.append(p.stdout.read(1))
        if out == '' and p.poll() != None:
            break
        if out != '':
            result.append(out)
    print(get)



image_into_tensdorflow("fdafd")