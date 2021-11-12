import cv2

img = cv2.imread('data/images/new_id_card.png', 0)
print(img)
# img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('data/images/new_id_card1.jpg', img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# results = ready.readtext('data/images/permis-de-conduire2.png')
