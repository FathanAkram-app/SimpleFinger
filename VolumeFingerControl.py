from Trackers.HandTracker import handDetector
import cv2

import time


cap = cv2.VideoCapture(0)
thumbId,indexId = 4, 8
pTime = 0
cTime = 0
detector = handDetector(detectionCon=0.7)
while True:
    # success, processed_img = cap.read()
    
    success, image = cap.read()
    processed_img, hand_landmarks = detector.find_hands(image)
    # processed_img = 

    img_height, img_width, _ = processed_img.shape
    positions = []
    if len(hand_landmarks) > 0:
        
        for id, lm in enumerate(hand_landmarks[0].landmark):
            
            if id == thumbId or id == indexId:
                posY = lm.y * img_height
                posX = lm.x * img_width

                positions.append([int(posX),int(posY)])
                # print(thumbPosX)  
                
        for i in positions:
            cv2.circle(processed_img,(i[0],i[1]),15,(255,255,0),5)
        
        cv2.line(processed_img,(positions[0][0],positions[0][1]),(positions[1][0],positions[1][1]),(231,123,32),4)




    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.putText(processed_img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3, (0,255,0), 3)

    cv2.imshow("WEBCAM", processed_img)
    cv2.waitKey(1)