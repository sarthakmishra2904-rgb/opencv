import cv2 as cv
img = cv.imread('ss.png')
cv.imshow('ss', img)

def rescaleFrame(frame, scale=0.75):
    #This function is used to rescale the frame of the video or image
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)    

cv.waitKey(0)

def changRes(width, height):
    #This function is used to change the resolution of the video
    capture.set(3, width)
    capture.set(4, height)
#rescaling videos

capture = cv.VideoCapture('gif.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)
    cv.imshow('gif', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()