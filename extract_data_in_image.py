import easyocr
import cv2

path_image = 'data/images/new_id_card.png'
img = cv2.imread(path_image, 0)
cv2.imshow('Image', img)
cv2.waitKey(10)
# cv2.destroyAllWindows()

reader = easyocr.Reader(['en', 'fr'])
results = reader.readtext(img)
# print(results)

text = '[ \n    { \n'
a = 0
for result in results:
    a = a + 1
    text += '       "champ '+str(a)+'" : "' + result[1] + '",\n'
text += '   } \n]'

file = open('data/output/image_data.txt', 'w')
file.write(text)
file.close()

print("fin - Samson")