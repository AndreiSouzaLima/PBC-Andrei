#Escreva um programa Python que leia uma imagem e faça o processamento de imagem, como redimensionamento, recorte ou aplicação de filtros.
import cv2

imagem = cv2.imread('imagem.png')

imagem_processada = cv2.GaussianBlur(imagem, (7, 7), 0)

cv2.imwrite('imagem_processada.png', imagem_processada)