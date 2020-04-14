import cv2,os
import numpy as np
from PIL import Image 
import time
import csv
import sys


img = sys.argv[1]
path = os.path.dirname(os.path.abspath(__file__))
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('./trainer/trainer.yml')
cascadePath = "./Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.imread(img)
font = cv2.FONT_HERSHEY_SIMPLEX

gray=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
for(x,y,w,h) in faces:
    nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
    cv2.rectangle(cam,(x-50,y-50),(x+w+50,y+h+50),(10,255,255), 2)

    with open('./data-face.csv') as csvfile:
        database = csv.DictReader(csvfile)
        for row in database:
            face_id = row['id']
            face_username = row['username']
            f_sign = row['face_sign']
            if str(nbr_predicted) == face_id:
                #print('Detected: ' + face_username)
                if conf < 65:
                    cv2.putText(cam,face_username+"--"+str(conf), (x,y+h),font, 1.1, (0,255,0),3)
                    print(face_username+"--"+str(conf)+ '--' +f_sign)
                else:
                    cv2.putText(cam,"unknown--"+str(conf), (x,y+h),font, 1.1, (0,255,0),3)
                    print("unknown--"+str(conf)) 
            else:
                cv2.putText(cam,"unknown--"+str(conf), (x,y+h),font, 1.1, (0,255,0),3)
                print("unknown--") 


    cv2.imshow('Recognition',cam)

cv2.destroyAllWindows()











