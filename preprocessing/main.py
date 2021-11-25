import cv2
import binarization as bin
import noise_removal as rm_noise


nom_image_et_extenxion = 'permis_de_conduire5.jpg'
path_input = '../data/images/' + nom_image_et_extenxion
img = cv2.imread(path_input)  # le param 0 permet de rendre l'image gris


image = bin.binarization(img)
no_noise = rm_noise.noise_removal(image)
cv2.imshow('Noise removal', no_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()