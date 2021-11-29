import cv2
import numpy as np
from scipy.interpolate import UnivariateSpline

image = cv2.imread('data/images/flou.png')


cv2.imshow('Original Image', image)
cv2.waitKey(0)

Gaussian = cv2.GaussianBlur(image, (1,1), 1)
cv2.imshow('image nooon flou', Gaussian)
cv2.waitKey(0)

median = cv2.medianBlur(image, 1)
cv2.imshow('Median Blurring', median)

cv2.waitKey(0)

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)



kernel = np.array([[-1,-1,-1], [-1, 9,-1], [-1,-1,-1]])
sharpened = cv2.filter2D(image, -1, kernel)
cv2.imshow('Bilateral Blurring', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()