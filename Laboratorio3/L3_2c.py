import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# Video Capture
cap = cv.VideoCapture(0)

# Obtém as dimensões do vídeo original
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# VideoWriter
out_origin = cv.VideoWriter("output_origin.webm", cv.VideoWriter_fourcc(*'VP80'), 20, (frame_width, frame_height))

# VideoWriter
out_mask = cv.VideoWriter("output_mask.webm", cv.VideoWriter_fourcc(*'VP80'), 20, (frame_width, frame_height))

# VideoWriter
out_res = cv.VideoWriter("output_res.webm", cv.VideoWriter_fourcc(*'VP80'), 20, (frame_width, frame_height))

while(True):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_orange = np.array([0, 100, 100])
    upper_orange = np.array([30, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_orange, upper_orange)
    # Apply Gaussian Bluer Filter
    mask_filter = cv.GaussianBlur(mask, (3, 3), 0)
    
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    # Escreve o frame no arquivo de vídeo
    out_origin.write(frame)
    # Escreve o frame no arquivo de vídeo
    out_mask.write(mask_filter)
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