import cv2 as cv
import numpy as np

blank = np.zeros((300, 300), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (270, 270), 255, -1)
circle = cv.circle(blank.copy(), (150, 150), 140, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)
#Bitwise OR

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

#Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

#Bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitwise_not)


cv.waitKey(0)
