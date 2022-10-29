import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
solucao_reconhecimento = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento.FaceDetection()
desenho = mp.solutions.drawing_utils






