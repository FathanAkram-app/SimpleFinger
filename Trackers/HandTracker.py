from tkinter.constants import NONE
import cv2
import mediapipe as mp



class handDetector():
    def __init__(self,mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon


        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, 
            self.maxHands,
            self.detectionCon,
            self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self,image):

            
            results = self.hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            
            hand_landmarks_result = []
            annotated_image = image.copy()
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    
                    hand_landmarks_result.append(hand_landmarks_result)

                    self.mpDraw.draw_landmarks(
                        annotated_image, 
                        hand_landmarks, 
                        self.mpHands.HAND_CONNECTIONS)

            return annotated_image, hand_landmarks_result

