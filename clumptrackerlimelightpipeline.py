#Clump Tracker V4 Anish Thakare, 22012 Loose Screws
import os
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

class Pollen:
    def __init__(self,x,y,radius,i):
        self.x=x
        self.y=y
        self.radius=radius
        self.i=i+1
    def pollenx(self):
        return self.x
    def polleny(self):
        return self.y
    def pollenrad(self):
        return 2.5*self.radius

def runPipeline(img, llrobot):
    llpython = []
    pollen_balls = []
    big_clump_list=[]
    root = os.getcwd()
    if img is None:
        print("IMAGE DID NOT LOAD")
        return
    img = cv.resize(img, (1280, 960), interpolation=cv.INTER_AREA)
    #  carefully tuned hsv mask
    hsv_frame=cv.cvtColor(img, cv.COLOR_BGR2HSV)
    low_yellow = np.array([16,68,100])
    high_yellow = np.array([35,255,255])
    yellow_mask = cv.inRange(hsv_frame, low_yellow, high_yellow)
    kernelC= np.ones((4,4), np.uint8)
    eroding = cv.erode(yellow_mask,kernelC)
    _, binary = cv.threshold(eroding, 127, 255, cv.THRESH_BINARY)
    floodfill = binary.copy() 
    h, w = binary.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv.floodFill(floodfill, mask, (0, 0), 255)
    floodfill_inv = cv.bitwise_not(floodfill)
    filled = binary | floodfill_inv
    filled = cv.resize(filled, (1920, 1440), interpolation=cv.INTER_AREA)
    filled = cv.medianBlur(filled, 21)
    filledRGB = cv.cvtColor(filled, cv.COLOR_GRAY2RGB)
    circles = cv.HoughCircles(filled, cv.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=17, minRadius=35, maxRadius=150)
    if circles is None:
        print("Hough found no circles.")
        return
    for i, circle in enumerate(circles[0, :]):
        x = int(circle[0])
        y = int(circle[1])
        r = int(circle[2])
        pollen = Pollen(x, y, r,i)
        pollen_balls.append(pollen)
    for pollen in pollen_balls:
            lx,rx,uy,dy=pollen.pollenx()-pollen.pollenrad(),pollen.pollenx()+pollen.pollenrad(),pollen.polleny()+pollen.pollenrad(),pollen.polleny()-pollen.pollenrad()
            each_clump=[]
            for pollen in pollen_balls:
                if pollen.pollenx()>=lx and pollen.pollenx()<=rx and pollen.polleny()>=dy and pollen.polleny()<=uy:
                    if pollen not in each_clump:
                        each_clump.append(pollen)
                    for clump in big_clump_list[:]:
                        if pollen in clump:
                            for ball in clump:
                                if ball!=pollen:
                                    if ball not in each_clump:
                                        each_clump.append(ball)
                            big_clump_list.remove(clump)
            big_clump_list.append(each_clump)
    contours, _ = cv.findContours(
    filled,
    cv.RETR_EXTERNAL,
    cv.CHAIN_APPROX_SIMPLE
    )
    largestContour = max(contours, key=cv.contourArea)
    x,y,w,h = cv.boundingRect(largestContour)
    # draw the unrotated bounding box
    cv.rectangle(filled,(x,y),(x+w,y+h),(0,255,255),2)
    return largestContour, filledRGB, llpython