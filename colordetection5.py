import cv2 as cv
import numpy as np
# cap = cv.VideoCapture(0)
img=cv.imread("/Users/rahulthakare/Downloads/clumpphotos/image2.jpeg")
while True:
    # _, frame=cap.read()
    hsv_frame=cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # #red
    # low_red = np.array([161, 155, 84])
    # high_red = np.array([179,255,255])
    #yellow
    low_yellow = np.array([16,68,100])
    high_yellow = np.array([35,255,255])
    
    
    yellow_mask = cv.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv.bitwise_and(hsv_frame, hsv_frame, mask=yellow_mask)

    kernelE = np.ones((13,13),np.uint8)
    kernelD = np.ones((3,3),np.uint8)
    kernelC= np.ones((7,7), np.uint8)
    kernelO= np.ones((13,13), np.uint8)
    erosion = cv.erode(yellow_mask, kernelE)
    dilation = cv.dilate(erosion, kernelD)
    closing = cv.morphologyEx(yellow_mask, cv.MORPH_CLOSE, kernelC)
    opening = cv.morphologyEx(yellow_mask, cv.MORPH_OPEN, kernelO)
        #cv.imshow("Frame", )
    #cv.imshow("Frame", )
    # cv.imshow("Red Mask", mask)
    cv.imshow("Yellow mask", yellow_mask)
    cv.imshow("E yellow mask", erosion)
    cv.imshow("E+D yellow mask", dilation)
    cv.imshow("CLosing yellow mask", closing)
    cv.imshow("opening yellow mask", opening)
    key=cv.waitKey(1)
    if key==ord('q'):
        break
print("User exited the program.")