import cv2
import urllib.request
from datetime import datetime


face_cascade = cv2.CascadeClassifier('C:\\Users\\andym\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\andym\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_eye_tree_eyeglasses.xml')


while True:
    urllib.request.urlretrieve("http://thispersondoesnotexist.com", "image.jpg")
    start = datetime.now()

    # Statements



    img = cv2.imread("image.jpg")

    r = 500.0 / img.shape[1]
    dim = (500, int(img.shape[0] * r))

    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


    grey = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    c = 0
    x1,x2 = 0,0
    for (x,y,w,h) in faces:
        #cv2.rectangle(resized,(x,y),(x+w,y+h),(255,0,0),2)
        roi_grey = grey[y:y+h, x:x+w]
        roi_color = resized[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_grey)
        face_left,face_right = x,x+w

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,0),-1)
        
    cv2.imshow('img',resized)
    cv2.waitKey(0)
