import glob
import os.path
import tensorflow as tf
import numpy as np
import cv2
import pyttsx3


class EvalManager(object):
    PD_PATH = 'model/nn.pb'
    IMG_PATH = 'predict_images/'
    strings = ['雏菊', '玫瑰花', '向日葵', '蒲公英', '郁金香']

    def __init__(self):
        super(object, self).__init__()

    def id_to_string(self, node_id):
        return self.strings[node_id]

    def init(self):
        with tf.gfile.FastGFile(self.PD_PATH, 'rb') as f:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(f.read())
            tf.import_graph_def(graph_def, name='')

    def predict_batch(self):
        result = []
        with tf.Session() as sess:
            softmax_tensor = sess.graph.get_tensor_by_name('output/prob:0')
            # 遍历目录
            for root, dirs, files in os.walk(self.IMG_PATH):
                for file in files:
                    result.append("图片名:" + file)
                    # 载入图片
                    image_data = tf.gfile.FastGFile(
                        os.path.join(root, file), 'rb').read()
                    predictions = sess.run(
                        softmax_tensor, {'DecodeJpeg/contents:0': image_data})  # 图片格式是jpg格式
                    predictions = np.squeeze(predictions)  # 把结果转为1维数据

                    # 打印图片路径及名称
                    image_path = os.path.join(root, file)

                    # 排序
                    top_k = predictions.argsort()[::-1]
                    for node_id in top_k:
                        # 获取分类名称
                        human_string = self.id_to_string(node_id)
                        # 获取该分类的置信度
                        score = predictions[node_id]
                        result.append('%s (score = %.5f)' %
                                      (human_string, score))
                    text = "本次预测的结果是" + self.id_to_string(top_k[0])
                    voice=pyttsx3.init()
                    voice.say(text)
                    voice.runAndWait()
                    # result.append(text + "\n")                    
        return result
                    

    def predict_single(self, image):
        print(image)
        result = []
        with tf.Session() as sess:
            softmax_tensor = sess.graph.get_tensor_by_name('output/prob:0')
            # 遍历目录
            # 载入图片
            image_data = tf.gfile.FastGFile(
                os.path.join(image), 'rb').read()
            predictions = sess.run(
                softmax_tensor, {'DecodeJpeg/contents:0': image_data})  # 图片格式是 jpg 格式
            predictions = np.squeeze(predictions)  # 把结果转为1维数据

            # 排序
            top_k = predictions.argsort()[::-1]
            for node_id in top_k:
                    # 获取分类名称
                human_string = self.id_to_string(node_id)
                # 获取该分类的置信度
                score = predictions[node_id]
                result.append('%s (score = %.5f)' %
                              (human_string, score))
            text = "本次预测的结果是"+self.id_to_string(top_k[0])
            voice=pyttsx3.init()
            voice.say(text)
            voice.runAndWait()
            result.append(text)
        return result
