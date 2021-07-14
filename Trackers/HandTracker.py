import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def hand_tracker(cap):
    with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        success, image = cap.read()
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        
        image_height, image_width, _ = image.shape
        annotated_image = image.copy()
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                indexTip = [
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y]

                middleTip = [
                    hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x,
                    hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                ]
                
                thumbTip = [
                    hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x,
                    hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
                ]

                ringTip = [
                    hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x,
                    hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
                ]

                pinkyTip = [
                    hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x,
                    hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y
                ]

                handWrist = [
                    hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x,
                    hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
                ]
                print(indexTip[1])
                print(thumbTip[1])
                print(handWrist[1])
                # if indexTip[1]



                mp_drawing.draw_landmarks(
                    annotated_image, 
                    hand_landmarks, 
                    mp_hands.HAND_CONNECTIONS)

        return False,annotated_image