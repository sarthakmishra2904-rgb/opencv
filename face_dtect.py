import cv2 as cv

img = cv.imread('ss.png')   
cv,cv.imshow('ss', img) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

haar_casscade = cv.CascadeClassifier('haar_face.xml')   

faces_rect = haar_casscade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detected Faces', img)
cv.waitKey(0)   