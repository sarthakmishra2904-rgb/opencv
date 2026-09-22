import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('ss.png')
cv.imshow('ss', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray) 

#Grayscale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
print(gray_hist.shape)

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

