#EYE RECOGNITION

import cv2
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('abc.jpg') #reading the image



eyes = eye_cascade.detectMultiScale(img,scaleFactor = 1.1,minNeighbors =20)



for x,y,w,h in eyes:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.imshow('FACE RECOGNITION',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
