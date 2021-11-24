import cv2
import numpy as np
from scipy.constants import value

img = cv2.imread('data/images/sombre.png')
cols, rows,npp = img.shape
brightness = np.sum(img) / (255 * cols * rows)
minimum_brightness = 0.66
alpha = brightness / minimum_brightness
bright_img = cv2.convertScaleAbs(img, alpha = alpha, beta = 255 * (1 - alpha))
bright_img11 = cv2.convertScaleAbs(img, alpha = 1, beta = 128)
bright_img1 = cv2.convertScaleAbs(img, alpha = 1, beta = 255 * (minimum_brightness - brightness))


cv2.imshow('origin', img)

cv2.imshow('Bilateral', bright_img)

cv2.imshow('Bilateralurring', bright_img1)
cv2.imshow('Bilate Blurring', bright_img11)

cv2.waitKey(0)
cv2.destroyAllWindows()

