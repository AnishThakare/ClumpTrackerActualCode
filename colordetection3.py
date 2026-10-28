import cv2 as cv
import time

cap=cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 728)
time.sleep(1)
while True:
    _, frame=cap.read()
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    height, width, _ =frame.shape
    cx=int(width/2)
    cy=int(height/2)
    
    pixel_center=hsv_frame[cy,cx]
    pixel_center_bgr = frame[cy,cx]
    color = "Undefined"
    hue_value = pixel_center[0]
    if hue_value < 5:
        color = "Red"
    elif hue_value < 22:
        color = "Orange"
    elif hue_value < 33:
        color="Yellow"
    elif hue_value < 78:
        color ="Green"
    elif hue_value<131:
        color = "Blue"
    elif hue_value<170:
        color = "Violet"
    else:
        color ="Red"
    # if int(pixel_center[0])>70 and int(pixel_center[0])<100 and int(pixel_center[1])>150 and int(pixel_center[1])<210 and int(pixel_center[2])>220 and int(pixel_center[2])<256:
    #     print("Yellow ball detected.")
    # pixel_center_bgr= frame[cx,cy]
    b, g, r, = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    # cv.putText(frame, color, (10,50), 0, 1, (b,g,r), 2 )
    h, s, v = pixel_center

    cv.putText(
        frame,
        f"H:{h} S:{s} V:{v}",
        (10, 50),
        cv.FONT_HERSHEY_SIMPLEX,
        0.8,
        (b,g, r),
        2
    )
    cv.circle(frame,(cx,cy),10,(b,g,r),8)
    cv.imshow("Anish", frame)
    key = cv.waitKey(1) 
    if key == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
print("yo ")