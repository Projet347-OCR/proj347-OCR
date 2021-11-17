import cv2
import numpy as np
import matplotlib as plt

# img = cv2.imread('data/images/carte_identite.png', 1)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower_blue = np.array([110, 50, 50])
# upper_blue = np.array([130, 255, 255])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
# result = cv2.bitwise_and(img, img, mask=mask)
# img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
# cv2.imwrite('data/images/new_id_card1.jpg', img)
# cv2.imshow('Image 1', img)
# cv2.imshow('Image 2', hsv)
# cv2.imshow('Image 2', mask)
#v cv2.waitKey(0)
# cv2.destroyAllWindows()
# results = ready.readtext('data/images/permis-de-conduire2.png')

### Detection d'angle - corner detection


'''img = cv2.imread('data/images/permis_de_conduire2.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
operatedImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
operatedImage = np.float32(operatedImage)
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)
dest = cv2.dilate(dest, None)
img[dest > 0.01 * dest.max()] = [0, 0, 255]'''

# corners = cv2.goodFeaturesToTrack(img, 100, 0.01, 10)
# corners = np.int0(corners)

# for corner in corners:
#     x, y = corner.ravel()
#     print(x, " et ", y)
    # cv2.circle(img, (x, y), 5, (255, 0, 0), -1)


kernel = np.ones((0,0), np.uint8)

img = cv2.imread('data/images/flou.png', 0)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
morph_grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


cv2.imshow('Erosion', erosion)
cv2.imwrite('data/images/er.jpg', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.imshow('Morphological Gradient', morph_grad)
cv2.imshow('Top Hat', top_hat)
cv2.imshow('Black Hat', black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()