import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math as m
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

######################################
wCam, hCam = 648, 480
######################################


cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# print(volume.GetVolumeRange())
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    # lmlist = []
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:
        # print(lmlist[4], lmlist[8])

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        cx, cy = int((x1+x2)/2), int((y1+y2)/2)
        cv2.circle(img, (x1, y1), 3, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 3, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        length = m.hypot(x2-x1, y2-y1)
        # print(length)

        # handrange 15-85
        # vol range -63.5  to 0

        vol = np.interp(length, [20, 260], [minVol, maxVol])
        # print(vol)

        volume.SetMasterVolumeLevel(vol, None)

        if length < 20:
            cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS:{int(fps)}', (40, 40),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 3)
    cv2.imshow("img:", img)
    cv2.waitKey(1)
