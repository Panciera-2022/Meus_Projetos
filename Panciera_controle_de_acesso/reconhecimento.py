import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
solucao_reconhecimento = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento.FaceDetection()
desenho = mp.solutions.drawing_utils






while True:
    # 1-Ler as informações da webcam
    verificador, imagem = webcam.read()
    if not verificador:
        break
    # 2-Reconhecer os rostos que tem ali dentro
    lista_rostos = reconhecedor_rostos.process(imagem)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # 3-Desenhar os rostos na imagem
            desenho.draw_detection(imagem, rosto)
    cv2.imshow('Rostos', imagem)

    # 4-Quando apertar ESC, sair do loop
    if cv2.waitKey(5) == 27:
        break










