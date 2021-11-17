import cv2
import numpy as np

kernel = np.ones((0,0), np.uint8)

img = cv2.imread('data/images/flou.png', 0)

image_flou = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)



cv2.imshow('Black Hat', black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
