import cv2
import numpy as np
import inverted as inv


def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def binarization(img):
    img = inv.inversed(img)
    gray_img = grayscale(img)
    cv2.imshow('Image Binarisee', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    thresh, im_bw = cv2.threshold(gray_img, 105, 255, cv2.THRESH_BINARY)
    cv2.imshow('Image binarisee sans fond', im_bw)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    kernel = np.ones((1, 1), np.uint8)
    erosion = cv2.erode(im_bw, kernel, iterations=1)
    cv2.imshow('Erosion appliquee a l_image binarisee sans fond', erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return im_bw