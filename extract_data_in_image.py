import easyocr

ready = easyocr.Reader(['en', 'fr'])
results = ready.readtext('data/images/permis-de-conduire2.png')
# print(results)

text = '[ \n    { \n'
a = 0
for result in results:
    a = a + 1
    text += '       "champ '+str(a)+'" : "' + result[1] + '",\n'
text += '   } \n]'

file = open('data/texte/image_data.txt', 'w')
file.write(text)
file.close()