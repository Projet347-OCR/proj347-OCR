import easyocr
import cv2

path_input = '../data/images/permis_de_conduire2.png'
path_output = '../data/output/image_data.txt'

img = cv2.imread(path_input, 0)
inverted_img = cv2.bitwise_not(img)
reader = easyocr.Reader(['fr', 'en'])
results = reader.readtext(inverted_img)
# print(results)

L = list()

for result in results:
    L.append(result[1])

text = str(L)

# text = '[ \n    { \n'
# a = 0
# for result in results:
#     a = a + 1
#     text += '       "champ '+str(a)+'" : "' + result[1] + '",\n'
# text += '   } \n]'

file = open(path_output, 'w')
file.write(text)
file.close()

print("fin - Samson")