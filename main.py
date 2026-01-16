import cv2
import mediapipe as mp
import os

face_mesh = mp.solutions.face_mesh.FaceMesh(
    min_detection_confidence=0.6,
    min_tracking_confidence= 0.7
    max_num_face=2
    refine_landmarks=True
)

cam0 = cv2.VideoCapture(0)
cam1 = cv2.VideoCapture(1)

#Thresholds 
open_eye = 0.025
open_mouth = 0.03
squinting = 0.018
tongue_out = 0.035
iris_look_left=0.4

def shakespear_meme(face_landmarks_points):
     