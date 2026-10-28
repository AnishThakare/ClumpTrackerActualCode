#Clump Tracker V3 Anish Thakare, 22012 Loose Screws
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
# class Clump:
#     def __init__(self,num,):
#     self.num=
pollen_balls = []
big_clump_list=[]
def pollen_extractor():
    root = os.getcwd()
    img = cv.imread("/Users/rahulthakare/Downloads/clumpphotos/image1.jpeg")
    img = cv.resize(img, (1280, 960), interpolation=cv.INTER_AREA)
    if img is None:
        print("IMAGE DID NOT LOAD")
        return
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
        cv.circle(filledRGB, (x, y), r, ((x/6), (y/6), 2),10)
        cv.putText(
        filledRGB,
        str(i + 1),
        (x - 10, y + 10),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
        )
    plt.figure("Figure 2")
    plt.imshow(filledRGB, )
    plt.show()
    for pollen in pollen_balls:
        lx,rx,uy,dy=pollen.pollenx()-pollen.pollenrad(),pollen.pollenx()+pollen.pollenrad(),pollen.polleny()+pollen.pollenrad(),pollen.polleny()-pollen.pollenrad()
        each_clump=[]
        for pollen in pollen_balls:
            if pollen.pollenx()>=lx and pollen.pollenx()<=rx and pollen.polleny()>=dy and pollen.polleny()<=uy:
                each_clump.append(pollen)
        big_clump_list.append(each_clump)
        
    for clump in big_clump_list:
        for ball in clump:
            print(f"x: {ball.x}, y: {ball.y}, radius: {ball.radius}, i: {ball.i}")
        print("-"*25)
    for pollen in pollen_balls:
        print(pollen.x, pollen.y, pollen.radius)
    print("User exited the program.")
if __name__ == "__main__":
    pollen_extractor()