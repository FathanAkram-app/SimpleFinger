
from Trackers.HandTracker import handDetector
import cv2
import time

cap = cv2.VideoCapture(0)

pTime = 0
cTime = 0

while True:
    # success, processed_img = cap.read()
    detector = handDetector()
    success, image = cap.read()
    processed_img, hand_landmarks = detector.find_hands(image)
    # processed_img = 

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(processed_img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3, (0,255,0), 3)

    cv2.imshow("WEBCAM", processed_img)
    cv2.waitKey(1)