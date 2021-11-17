import cv2
import numpy as np

path_input = '../data/images/carte_identite5.jpg'
kernel = np.ones((0, 0), np.uint8)

img = cv2.imread(path_input, 0)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
morph_grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.imshow('Morphological Gradient', morph_grad)
cv2.imshow('Top Hat', top_hat)
cv2.imshow('Black Hat', black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()