import cv2 as cv
import numpy as np

img = cv.imread('ss.png')
cv.imshow('ss', img)

b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r) 

blue = cv.merge([b, np.zeros_like(b), np.zeros_like(b)])
green = cv.merge([np.zeros_like(g), g, np.zeros_like(g)])
cv.imshow('Blue Merged', blue)
cv.imshow('Green Merged', green)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)