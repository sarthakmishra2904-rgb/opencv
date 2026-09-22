import cv2 as cv
import numpy as np

img = cv.imread('ss.png')
cv.imshow('ss', img)

blank = np.zeros((300, 300), dtype='uint8')
cv.imshow('Blank', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)