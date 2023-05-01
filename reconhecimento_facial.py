#Escreva um programa Python que leia um arquivo de vídeo e faça o processamento de vídeo, como detecção de objetos ou reconhecimento facial.
import cv2

captura = cv2.VideoCapture('video.mp4')

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

codec = cv2.VideoWriter_fourcc(*'XVID')


gravacao = cv2.VideoWriter('video_processado.avi', codec, 30.0, (640, 480))

while True:
    ret, quadro = captura.read()

    if not ret:
        break

    cinza = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(quadro, (x, y), (x+w, y+h), (0, 255, 0), 2)

    gravacao.write(quadro)

captura.release()
gravacao.release()