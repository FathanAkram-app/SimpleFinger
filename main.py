
import cv2
import mediapipe as mp
import PySimpleGUI as sg
import Trackers.HandTracker as HandTracker

USE_CAMERA = 0      # change to 1 for front facing camera
window = sg.Window(
  'DrawBody', 
  [
    [sg.Image(filename='', key='image')], 
    [
      sg.Button(
      button_text="Turn On Peace to capture",)
      
    ]
  ], 
  location=(0, 0), 
  grab_anywhere=True)

cap = cv2.VideoCapture(USE_CAMERA)

while window(timeout=20)[0] != sg.WIN_CLOSED:
    isPeace, processedImage = HandTracker.hand_tracker(cap)
    window['image'](data=cv2.imencode('.png', processedImage)[1].tobytes())