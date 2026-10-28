#Circle detection using Hough Transform
import os

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def hough_circle_detection():
    root = os.getcwd()
    # imgPath=os.path.join(root, "clumpphotos","image1.jpeg")
    img = cv.imread("/Users/rahulthakare/Downloads/clumpphotos/maskedballs4.png")
    img1 = cv.imread("/Users/rahulthakare/Downloads/clumpphotos/maskedballs4.png")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Turn the mask into pure black/white
    _, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

    # Fill enclosed black holes
    floodfill = binary.copy()

    h, w = binary.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)

    cv.floodFill(floodfill, mask, (0, 0), 255)

    floodfill_inv = cv.bitwise_not(floodfill)

    filled = binary | floodfill_inv
    # img1= cv.imread("/Users/rahulthakare/Downloads/clumpphotos/maskedballs2.png")
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgGray = filled
    plt.figure()
    plt.imshow(filled, cmap="gray")
    plt.show()
    # circles = cv.HoughCircles(imgGray, cv.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=19, minRadius=60, maxRadius=140)
    # if circles is None:
    #     print("No circles detected")
    #     return

    # for circle in circles[0, :]:
    #     x = int(circle[0])
    #     y = int(circle[1])
    #     r = int(circle[2])
    #     cv.circle(imgRGB, (x, y), r, (255, 0, 0), 10)
    plt.figure()
    plt.imshow(img1)
    plt.show()

if __name__ == "__main__":
    hough_circle_detection()
    