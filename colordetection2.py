import cv2 as cv
import time

cap=cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 728)
time.sleep(1)
while True:
    _, frame=cap.read()

    height, width, _ =frame.shape
    cx=int(width/2)
    cy=int(height/2)

    pixel_center=frame[cy,cx]
    if int(pixel_center[0])>70 and int(pixel_center[0])<100 and int(pixel_center[1])>150 and int(pixel_center[1])<210 and int(pixel_center[2])>220 and int(pixel_center[2])<256:
        print("Yellow ball detected.")
    # time.sleep(.1)
    cv.circle(frame,(cx,cy),10,(80,25,200),8)
    cv.imshow("Anish", frame)
    key = cv.waitKey(1) 
    if key == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
print("yo ")