
import cv2
import time
import os
import HandTrackingModule as htm
from control import PressKey, ReleaseKey
from pynput.keyboard import Key, Controller
break_key_pressed = Key.left
accelerato_key_pressed = Key.right
wCam, hCam = 640, 480
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
folderPath = "FingerImages"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
pTime = 0
detector = htm.handDetector(detectionCon=0.5)
tipIds = [4, 8, 12, 16, 20]
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        fingers = []
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        totalFingers = fingers.count(1)
        if totalFingers == 0:
            cv2.rectangle(image, (20, 300), (270, 425),
                          (0, 255, 0), cv2.FILLED)
            cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
            PressKey(break_key_pressed)
            break_pressed = True
            current_key_pressed.add(break_key_pressed)
            key_pressed = break_key_pressed
            keyPressed = True
            key_count = key_count+1
        elif totalFingers == 5:
            cv2.rectangle(image, (20, 300), (270, 425),
                          (0, 255, 0), cv2.FILLED)
            cv2.putText(image, " GAS", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (255, 0, 0), 5)
            PressKey(accelerato_key_pressed)
            key_pressed = accelerato_key_pressed
            accelerator_pressed = True
            keyPressed = True
            current_key_pressed.add(accelerato_key_pressed)
            key_count = key_count+1
        elif totalFingers == 2:
            PressKey(Key.space)
            ReleaseKey(Key.space)
    if not keyPressed and len(current_key_pressed) != 0:
        for key in current_key_pressed:
            ReleaseKey(key)
        current_key_pressed = set()
    elif key_count == 1 and len(current_key_pressed) == 2:
        for key in current_key_pressed:
            if key_pressed != key:
                ReleaseKey(key)
        current_key_pressed = set()
        for key in current_key_pressed:
            ReleaseKey(key)
        current_key_pressed = set()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
