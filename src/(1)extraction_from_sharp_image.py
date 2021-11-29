import easyocr
import cv2

# path_input = '../data/images/carte_identite4.jpeg'
path_input = '../data/images/(1)carte_identite3.jpg'
path_output = '../data/output/image_data.txt'

img = cv2.imread(path_input, 0)
reader = easyocr.Reader(['fr', 'en'])
results = reader.readtext(img)

L = list()

for result in results:
    L.append(result[1])

# print(L)
texte = 'PAYS : '+str(L[0])+'\n'
texte += 'TYPE DE PIECE : '+str(L[2])+'\n'
texte += 'NOM(S) : '+str(L[5])+'\n'
texte += 'PRENOM(S) : '+str(L[8])+'\n'
texte += 'SEXE : '+str(L[13])+'\n'
texte += 'NATIONALITE : '+str(L[14])+'\n'
texte += 'DATE DE NAISSANCE : '+str(L[15])+'\n'
texte += 'LIEU DE NAISSANCE : '+str(L[18])+'\n'
texte += 'NOM D_USAGE : '+str(L[20])+'\n'
texte += 'NUMERO DOCUMENT : '+str(L[23])+'\n'
texte += 'DATE EXPIRATION : '+str(L[24])
print(texte)


file = open(path_output, 'w')
file.write(str(texte))
file.close()
