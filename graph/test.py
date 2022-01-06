import cv2


img_recto = '../data/images/ci1-recto.png'
img_verso = '../data/images/ci1-verso.png'

imgr = cv2.imread(img_recto, 0)
imgv = cv2.imread(img_verso, 0)

# Inversion
inverted_imgr = cv2.bitwise_not(imgr)
inverted_imgv = cv2.bitwise_not(imgv)

cv2.imshow("Image avant normal", img_recto)
cv2.imshow("Image avant binarisee", inverted_imgr)

cv2.imshow("Image avant normal", img_verso)
cv2.imshow("Image avant binarisee", inverted_imgv)

cv2.waitKey(0)
cv2.destroyAllWindows()