import cv2


def inversed(img):
    inverted_img = cv2.bitwise_not(img)
    cv2.imshow('Image originale grisee', img)
    cv2.imshow('Image inversee', inverted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return inverted_img