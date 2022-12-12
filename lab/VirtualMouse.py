#make a AI virtual mouse with opencv
import cv2
import numpy as np
import Hand_Tracking_Module as htm
import time
import pyautogui
import mediapipe as mp

class VirtualMouse:
    def __init__(self):
        self.wCam, self.hCam = 640, 480
        self.frameR = 100
        self.smoothening = 7
        self.pTime = 0
        self.plocX, self.plocY = 0, 0
        self.clocX, self.clocY = 0, 0
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.wCam)
        self.cap.set(4, self.hCam)
        self.detector = htm.handDetector(maxHands=1)
        self.wScr, self.hScr = pyautogui.size()
        self.frameR = 100
        self.smoothening = 7

    def findDistance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return length

    def mouseControl(self):
        while True:
            success, img = self.cap.read()
            img = self.detector.findHands(img)
            lmList, bbox = self.detector.findPosition(img)
            if len(lmList) != 0:
                x1, y1 = lmList[8][1:]
                x2, y2 = lmList[12][1:]
                fingers = self.detector.fingersUp()
                cv2.rectangle(img, (self.frameR, self.frameR), (self.wCam - self.frameR, self.hCam - self.frameR), (255, 0, 255), 2)
                if fingers[1] == 1 and fingers[2] == 0:
                    x3 = np.interp(x1, (self.frameR, self.wCam - self.frameR), (0, self.wScr))
                    y3 = np.interp(y1, (self.frameR, self.hCam - self.frameR), (0, self.hScr))
                    clocX = self.plocX + (x3 - self.plocX) / self.smoothening
                    clocY = self.plocY + (y3 - self.plocY) / self.smoothening
                    pyautogui.moveTo(self.wScr - clocX, clocY)
                    cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                    self.plocX, self.plocY = clocX, clocY
                if fingers[1] == 1 and fingers[2] == 1:
                    length, img, lineInfo = self.detector.findDistance(8, 12, img)
                    if length < 40:
                        cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                        pyautogui.click()
            cTime = time.time()
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.imshow("Image", img)
            cv2.waitKey(1)

if __name__ == '__main__':
    mouse = VirtualMouse()
    mouse.mouseControl()