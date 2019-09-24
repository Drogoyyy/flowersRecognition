import glob
import os.path
import tensorflow as tf
import numpy as np
import cv2
import pyttsx3

def predict():        
    # strings = ['daisy', 'roses', 'sunflowers', 'dandelion', 'tulips']
    strings = ['雏菊', '玫瑰花', '向日葵', '蒲公英', '郁金香']
    def id_to_string(node_id):
        return strings[node_id]
 
    with tf.gfile.FastGFile('C:/Users/82622/Desktop/flowersRecognition/model/nn.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')
 
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('output/prob:0')
        # 遍历目录
        for root, dirs, files in os.walk('C:/Users/82622/Desktop/flowersRecognition/predict_images/'):
            for file in files:
                # 载入图片
                image_data = tf.gfile.FastGFile(os.path.join(root, file), 'rb').read()
                predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image_data})  # 图片格式是jpg格式
                predictions = np.squeeze(predictions)  # 把结果转为1维数据
 
                # 打印图片路径及名称
                image_path = os.path.join(root, file)            
                print("=========================================")
                print(image_path)
 
                # 排序
                top_k = predictions.argsort()[::-1]
                print(top_k)
                for node_id in top_k:
                    # 获取分类名称
                    human_string = id_to_string(node_id)
                    # 获取该分类的置信度
                    score = predictions[node_id]
                    print('%s (score = %.5f)' % (human_string, score))
                print("预测的结果是"+id_to_string(top_k[0]))
                text = "本次预测的结果是"+id_to_string(top_k[0])                
                img = cv2.imread(image_path)
                cv2.imshow('image', img)
                voice=pyttsx3.init()
                voice.say(text)
                voice.runAndWait()
                cv2.waitKey(0)
    cv2.destroyAllWindows()

predict()