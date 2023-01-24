import cv2 
import numpy as np
import os ,json
def check_for_login(id):
    data=[]
    with open('data_player/data.json') as file_name:
        data=json.load(file_name)
    cascadePath="haarcascade_frontalface_default.xml"
    faceCascade= cv2.CascadeClassifier(cv2.data.haarcascades + cascadePath)
    cam=cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    minW=0.1*cam.get(3)
    minH=0.1*cam.get(4)
    font=cv2.FONT_HERSHEY_SIMPLEX
    count=0
    recognizer= cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer_id='+str(id)+".yml")
    user_name="unknowm"
    checking=True
    count=0
    list_username=[]
    while checking:
        ret,img=cam.read()
        img=cv2.flip(img,-1)
        img=cv2.rotate(img,cv2.ROTATE_180)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW),int(minH)),
        )
        count+=1
        if count>=300:
            break
        # print(user_name)
        for (x,y,w,h) in faces :
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
            id , confidence=recognizer.predict(gray[y:y+h, x:x+w])
            if (confidence<100):
                user_name=data[0]['user'][id]['user_name']
                confidence=" {0}%".format(round(100-confidence))
                # print("ok")
            else:
                user_name ="unknowm"
                confidence= " {0}%".format(round(100-confidence))
            cv2.putText(img,str(user_name), (x+5,y-5),font,1,(255,255,255),2)
            cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
            list_username.append(user_name)
        #cv2.imshow('nhan dien khuon mat',img)
        k= cv2.waitKey(10) & 0xff
        if k ==27 :
            break 
    # print(" da nhan dien xong ",id)
    cam.release()
    cv2.destroyAllWindows()
    count_user=0
    for user in list_username:
        if user!="unknowm":
            count_user+=1
    if count_user<10:
        return False
    else :
        return True
