import cv2 as cv
import numpy as np  

img = cv.imread('ss.png')

cv.imshow('ss', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray) 

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)  

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found!') 

cv.drawContours(img, contours, -1, (0, 255, 0), 2)  
cv.imshow('Contours Drawn', img)

cv.waitKey(0)
cv.destroyAllWindows()
