#Circle detection using Hough Transform
import os

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def hough_circle_detection():
    root = os.getcwd()
    # imgPath=os.path.join(root, "clumpphotos","image1.jpeg")
    img = cv.imread("/Users/rahulthakare/Downloads/clumpphotos/filledE4.png")
    # img1= cv.imread("/Users/rahulthakare/Downloads/clumpphotos/maskedballs2.png")
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgGray = cv.medianBlur(imgGray, 21)
    circles = cv.HoughCircles(imgGray, cv.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=27, minRadius=35, maxRadius=150)

    for circle in circles[0, :]:
        x = int(circle[0])
        y = int(circle[1])
        r = int(circle[2])
        cv.circle(imgRGB, (x, y), r, (255, 0, 0), 10)
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == "__main__":
    hough_circle_detection()