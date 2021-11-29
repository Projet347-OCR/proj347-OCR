import easyocr
import cv2

path_input = '../data/images/(2)carte_identite1.png'
#path_input = '../data/images/carte_identite2.jpg'
path_output = '../data/output/image_data.txt'


img = cv2.imread(path_input, 0)
reader = easyocr.Reader(['fr', 'en'])
results = reader.readtext(img)

L = list()

for result in results:
    L.append(result[1])

print(L)
texte = 'PAYS : '+str(L[0])+' '+str(L[1])+'\n'
texte += 'TYPE DE PIECE : '+str(L[2])+'\n'
texte += 'INITIALE : '+str(L[4])+'\n'
texte += 'NOM(S) : '+str(L[6])+'\n'
texte += str(L[7])+'\n'
# texte += 'SEXE : '+str(L[13])+'\n'
texte += str(L[3])+'\n'
texte += str(L[9])+' '+str(L[10])+' ('+str(L[11])+')'+'\n'
texte += 'TAILLE : '+str(L[13])+'\n'
texte += str(L[2])+'\n'
texte += 'ID CARD : '+str(L[18]+' '+L[19])
print(texte)

file = open(path_output, 'w')
file.write(str(texte))
file.close()
