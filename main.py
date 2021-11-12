import easyocr
print('Projet347-OCR (Brandy)')

ready = easyocr.Reader(['en', 'fr'])

results = ready.readtext('data/images/MicrosoftTeams-image.png')

#print(results)

text = ''
a = 0
for result in results:
    a = a + 1
    text += 'Champ '+ str(a) + ' : ' + result[1] + '\n'

#print(text)
#print(len(results))

outfile = open('data/texte/test.txt', 'w')

outfile.write(text)
outfile.close()
