import cv2 as cv

img =cv.imread('ss.png')
cv.imshow('ss',img)
cv.waitKey(0)

#reading videos
capture = cv.VideoCapture('gif.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('gif', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()