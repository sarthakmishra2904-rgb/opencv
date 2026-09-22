import cv2 as cv
import numpy as np

blank =np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
#colouring the image
blank[:] = 0,255,0
cv.imshow('Green', blank)

#draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,0,255), thickness=2)
cv.imshow('Rectangle', blank)  
#draw a circle
cv.circle(blank, (250,250), 40, (255,0,0), thickness=2)
cv.imshow('Circle', blank)
#draw a line
cv.line(blank, (0,0), (500,500), (255,255,255), thickness=3)
cv.imshow('Line', blank)
#write text on image
cv.putText(blank, 'Hello', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), thickness=2)
cv.imshow('Text', blank)
cv.waitKey(0)