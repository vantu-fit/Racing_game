import cv2
import os ,shutil
def create_recognition(id,method):
    if method==1:
        shutil.rmtree('dataset/player_id='+str(id))
    os.mkdir('dataset/player_id='+str(id))
    cam = cv2.VideoCapture(0)
    cam.set(3,640)
    cam.set(4,480)
    face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    face_id=id
    print(" dang khoi tao camera ")
    count = 0
    while True:
        ret,img= cam.read()
        img =cv2.flip(img , -1) # flip video 
        img=cv2.rotate(img,cv2.ROTATE_180)
        gray= cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        faces= face_detector.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y) , (x+w,y+h), (255,0,0),2)
            count +=1
            cv2.imwrite('dataset/player_id='+str(face_id)+"/User." + str(face_id) +'.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            # cv2.imshow('imgage',img)
        k= cv2.waitKey(100) & 0xff
        if k == 27 :
            break
        elif count>=30:
            break
# create_recognition(2)