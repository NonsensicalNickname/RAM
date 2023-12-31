from cvzone.HandTrackingModule import HandDetector
import cv2
import time
from pyfirmata import Arduino, SERVO
import platform
import threading
#180 degrees is fully up, 0 is fully down
#for thumb, 360 is loose and 0 is tight
#fingersUp array is in order of thumb to pinky
fingerPins = [2,4,7,8,12]


if platform.system() == "Windows":
    port = "COM3"
else:
    port = "/dev/ttyUSB0"

board = Arduino(port)

for finger in fingerPins: #set the mode for each pin in use and move all fingers to initial position
    board.digital[finger].mode = SERVO
    if finger == 2:
        board.digital[finger].write(360)
    else:
        board.digital[finger].write(180)


print("Communication Successfully started")
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

def move(finger, pos): # move le finger to specified angle 
    currentPos = board.digital[finger].read()
    if currentPos > pos:
        while board.digital[finger].read() > pos:
                board.digital[finger].write(board.digital[finger].read() - 1)
                time.sleep(0.0025) 
    if currentPos < pos:
        while board.digital[finger].read() < pos:
            board.digital[finger].write(board.digital[finger].read() + 1)
            time.sleep(0.0025) 

def get(fingersUp): # determine what angle le finger should be moved to
    output = []
    fingerNum = 0
    for finger in fingersUp:
        if finger == 0:
            output.append(0)
        if finger == 1:
            if fingerNum == 0:
                output.append(360)
            else:
                output.append(180)
        fingerNum += 1
    return output 



while True:
    threads = []
    fingerNum = 0

    success, img = cap.read()
    hands, img = detector.findHands(img)  
    if hands:
        #get hand info 
        hand = hands[0]
        lmList = hand["lmList"] 
        bbox1 = hand["bbox"]
        centerPoint = hand['center'] 
        handType = hand["type"] 

        fingersUp = detector.fingersUp(hand)
        print(f"{handType} hand fingers up: {fingersUp}") 

        for finger in get(fingersUp): # add finger movements to thread list
            threads.append(threading.Thread(target=move(fingerPins[fingerNum], finger)))
            fingerNum += 1
    for th in threads:
        th.start() # start threads
    for th in threads:
        th.join() # wait for threads
    cv2.imshow("Image", img) # output frame
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
