#ccolor detection
import cv2 as cv
import os
img=cv.imread("blue_background.png")
print(img)
cv.imshow("BOI", img)
cv.waitKey(0)