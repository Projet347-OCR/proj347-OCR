import easyocr
import cv2

path_input = '../data/images/carte_identite5.jpg'
path_output = '../data/output/image_data.txt'

img = cv2.imread(path_input, 0)
reader = easyocr.Reader(['fr'])
results = reader.readtext(img)
# print(results)

text = '[ \n    { \n'
a = 0
for result in results:
    a = a + 1
    text += '       "champ '+str(a)+'" : "' + result[1] + '",\n'
text += '   } \n]'

file = open(path_output, 'w')
file.write(text)
file.close()

print("fin - Samson")