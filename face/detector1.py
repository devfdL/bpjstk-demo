import cv2,os
import numpy as np
from PIL import Image 
import time
import csv

path = os.path.dirname(os.path.abspath(__file__))

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('./trainer/trainer.yml')
cascadePath = "./Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

delay=6   
close_time=time.time()+delay
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
      nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
      cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(10,255,255), 2)

      with open('./data-face.csv') as csvfile:
            database = csv.DictReader(csvfile)
            for row in database:
                face_id = row['id']
                face_username = row['username']
                if str(nbr_predicted) == face_id:
                  #print('Detected: ' + face_username)
                  cv2.putText(im,face_username+"--"+str(conf), (x,y+h),font, 1.1, (0,255,0),3)
                else:
                  cv2.putText(im,"--"+str(conf), (x,y+h),font, 1.1, (0,255,0),3) 

      #cv2.putText(im,str(nbr_predicted)+"--"+str(conf), (x,y+h),font, 1.1, (0,0,0),3) #Draw the text
      cv2.imshow('Recognition',im)
      #cv2.waitKey(1)
      #print('Detected: '+ str(nbr_predicted))
      #print(len(faces))

  
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything is done, release the capture
cam.release()
cv2.destroyAllWindows()











