import cv2 
import numpy as np
from PIL import Image
import os
# khai bao duong dan 
def train_data_face(id):
    path = 'dataset/player_id='+str(id)
    # import models phat hien khuon mat
    recognizer= cv2.face.LBPHFaceRecognizer_create()
    detecter= cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    # lay label
    def getImagesAndLabels(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faceSamples = []
        ids =[]
        # for de lay id 
        for imagePath in imagePaths :
            PIL_img=Image.open(imagePath).convert('L')
            img_numpy= np.array(PIL_img,'uint8')
            #id = int(os.path.split(imagePath)[-1].split(".")[1]) # lay id tu path 
            faces=detecter.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            #.append(id)
        return faceSamples
    print(" dang train du lieu ")
    faces  = getImagesAndLabels(path)
    recognizer.train(faces,np.array(id))
    recognizer.write('trainer/trainer_id='+str(id)+".yml")
    print(" da train xong du lieu ")

# train_data_face(3)