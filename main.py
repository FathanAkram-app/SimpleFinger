
from Trackers.HandTracker import handDetector
import cv2
import mediapipe as mp
import PySimpleGUI as sg

USE_CAMERA = 0      # change to 1 for front facing camera
window = sg.Window(
  'DrawBody', 
  [
    [sg.Image(filename='', key='image')], 
    [
      sg.Button(
      button_text="Button1",)
      
    ]
  ], 
  location=(0, 0), 
  grab_anywhere=True)

cap = cv2.VideoCapture(USE_CAMERA)

while window(timeout=20)[0] != sg.WIN_CLOSED:
    success, image = cap.read()
    detector = handDetector()
    processedImage, hand_landmarks = detector.find_hands(image)
    
    window['image'](data=cv2.imencode('.png', processedImage)[1].tobytes())