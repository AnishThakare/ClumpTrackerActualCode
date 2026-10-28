import cv2 as cv
import numpy as np
import time
img=cv.imread("/Users/rahulthakare/Downloads/clumpphotos/filledballs4.png")
while True:
    kernel=np.ones((7,7), np.uint8)
    kernel1=np.ones((3,3), np.uint8)
    erodedimg=cv.erode(img,kernel1,iterations=1)
    closedimg=cv.dilate(erodedimg,kernel,iterations=1)
    cv.imshow("Before eroding", img)
    cv.imshow("After eroding", erodedimg)
    cv.imshow("After E+D", closedimg)
    key=cv.waitKey(1)
    if key==ord('q'):
            break
print("User exited the program.")