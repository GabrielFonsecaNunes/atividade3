import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)

while(True):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_orange = np.array([10, 150, 100])
    upper_orange = np.array([20, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_orange, upper_orange)
    # Apply Gaussian Bluer Filter
    mask_filter = cv.GaussianBlur(mask, (3, 3), 0)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    
    k = cv.waitKey(3)
    if k == ord("q"):
        cv.imwrite(filename="Controle_Original_b.jpg", img= frame)
        cv.imwrite(filename="Controle_Mask_b.jpg", img= mask)
        cv.imwrite(filename="Controle_Res_b.jpg", img = res)
        break

cv.destroyAllWindows()