import cv2 as cv

img = cv.imread('ss.png')
cv.imshow('ss', img)

#Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)   

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)
#Bilateral Blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)
cv.destroyAllWindows()