import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Video Capture
cap = cv.VideoCapture(0)

# Obtém as dimensões do vídeo original
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# VideoWriter
out_origin = cv.VideoWriter("output_origin_combined.webm", cv.VideoWriter_fourcc(*'VP80'), 20, (frame_width, frame_height))

# VideoWriter
out_mask = cv.VideoWriter("output_mask_combined.webm", cv.VideoWriter_fourcc(*'VP80'), 20, (frame_width, frame_height))

# VideoWriter
out_res = cv.VideoWriter("output_res_combined.webm", cv.VideoWriter_fourcc(*'VP80'), 20, (frame_width, frame_height))

while(True):
    # Take each frame
    _, frame = cap.read()

    # Apply Gaussian Bluer Filter
    frame = cv.GaussianBlur(frame, (3, 3), 0)

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([130,255,255])
    
    # define range of blue color in HSV
    lower_orange = np.array([0, 100, 100])
    upper_orange = np.array([30, 255, 255])

    # Criando as máscaras para as cores laranja e azul
    mask_orange = cv.inRange(hsv, lower_orange, upper_orange)
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)

    # Combinando as máscaras
    combined_mask = cv.bitwise_or(mask_orange, mask_blue)

    # Aplicando a máscara combinada à imagem original
    res = cv.bitwise_and(frame, frame, mask=combined_mask)
    
    cv.imshow('frame',frame)
    cv.imshow('mask',combined_mask)
    cv.imshow('res',res)

    # Escreve o frame no arquivo de vídeo
    out_origin.write(frame)
    # Escreve o frame no arquivo de vídeo
    out_mask.write(combined_mask)
    # Escreve o frame no arquivo de vídeo
    out_res.write(res)    

    q = cv.waitKey(3)
    if q == ord("q"):
        break

out_origin.release()
out_mask.release()
out_res.release()
cap.release()
cv.destroyAllWindows()