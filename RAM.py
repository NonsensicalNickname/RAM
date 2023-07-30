from cvzone.HandTrackingModule import HandDetector
import cv2
import time
from pyfirmata import Arduino, SERVO
import platform


if platform.system() == "Windows":
    port = "COM3"
else:
    port = "/dev/ttyUSB0"

board = Arduino(port)
board.digital[2].mode = SERVO
print("Communication Successfully started")
direction = 2
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
while True:
    if direction == 0:
        if board.digital[2].read() > 170:
            while board.digital[2].read() > 1:
                board.digital[2].write(board.digital[2].read() - 1)
                time.sleep(0.01) 

    if direction == 1:
        if board.digital[2].read() < 10:
            while board.digital[2].read() < 180:
                board.digital[2].write(board.digital[2].read() + 1)
                time.sleep(0.01) 



    success, img = cap.read()
    hands, img = detector.findHands(img)  
    if hands:
        hand = hands[0]
        lmList = hand["lmList"] 
        bbox1 = hand["bbox"] 
        centerPoint = hand['center'] 
        handType = hand["type"] 

        fingersUp = detector.fingersUp(hand)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
    print(f"{handType} hand fingers up: {fingersUp}")
    if fingersUp[2] == 0:
        direction = 0 #down
    else:
        direction = 1 #up
        
cap.release()
cv2.destroyAllWindows()
