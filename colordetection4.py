import cv2 as cv
import numpy as np
import time
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
    low_yellow_2 = np.array([16,68,170])
    high_yellow_2 = np.array([35,255,255])

    kernelC= np.ones((17,17), np.uint8)

    yellow_mask = cv.inRange(hsv_frame, low_yellow, high_yellow)
    yellow_mask_2 = cv.inRange(hsv_frame, low_yellow_2, high_yellow_2)
    yellow = cv.bitwise_and(hsv_frame, hsv_frame, mask=yellow_mask)
    closing = cv.morphologyEx(yellow_mask_2, cv.MORPH_CLOSE, kernelC)
    # dilation = cv.dilate()

    #cv.imshow("Frame", )
    # cv.imshow("Red Mask", mask)
    cv.imshow("Yellow mask", yellow_mask)
    cv.imshow("Yellow mask 2", yellow_mask_2)
    cv.imshow("Closed yellow mask", closing)
    key=cv.waitKey(1)
    if key==ord('q'):
        break
print("User exited the program.")