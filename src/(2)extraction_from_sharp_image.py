import easyocr
import cv2


img = cv2.imread('../data/images/ci4.jpg', 0)
reader = easyocr.Reader(['fr', 'en'])
results = reader.readtext(img)

L = list()

for result in results:
    L.append(result[1])
print(L)
t = str(L)
# texte = 'PAYS : '+str(L[0])+' '+str(L[1])+'\n'
# texte += 'TYPE DE PIECE : '+str(L[2])+'\n'
# texte += 'NOM(S) : '+str(L[5])+'\n'
# texte += str(L[7])+'\n'
# texte += 'SEXE : '+str(L[13])+'\n'
# texte += str(L[3])+'\n'
# texte += str(L[9])+' '+str(L[10])+' ('+str(L[11])+')'+'\n'
# texte += str(L[2])+'\n'
# texte += 'INITIALE : '+str(L[4])+'\n'
# texte += 'TAILLE : '+str(L[13])+'\n'

print(t)

file = open('../data/output/image_data.txt', 'w')
file.write(str(t))
file.close()



