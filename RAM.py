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
print("Communication Successfully started")
board.digital[2].mode = SERVO
board.digital[2].write(0)
for i in range(180):
    angle = i + 1
    board.digital[2].write(i)
    print(angle)              
    time.sleep(0.01) 

'''
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # with draw

    if hands:
        # Hand 1
        hand = hands[0]
        lmList = hand["lmList"]  # List of 21 Landmark points
        bbox1 = hand["bbox"]  # Bounding box info x,y,w,h
        centerPoint = hand['center']  # center of the hand cx,cy
        handType = hand["type"]  # Handtype Left or Right

        fingersUp = detector.fingersUp(hand)
        
        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"

            fingers2 = detector.fingersUp(hand2)

            # Find Distance between two Landmarks. Could be same hand or different hands
            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
        
        length, info, img = detector.findDistance(lmList[8], lmList[0], img)
        print(f"{handType} hand fingers up: {fingersUp}")
    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
cap.release()
cv2.destroyAllWindows()
'''