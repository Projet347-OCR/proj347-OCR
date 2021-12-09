import re
import easyocr
import cv2
import csv

img_recto = '../data/images/ci1-recto.png'
img_verso = '../data/images/ci1-verso.png'

imgr = cv2.imread(img_recto, 0)
imgv = cv2.imread(img_verso, 0)

# Inversion
inverted_imgr = cv2.bitwise_not(imgr)
inverted_imgv = cv2.bitwise_not(imgv)

reader = easyocr.Reader(['fr', 'en'])
results_r = reader.readtext(inverted_imgr)
results_v = reader.readtext(inverted_imgv)

for result in results_r:
    with open('../data/output/test_auto.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(str(result[1]))


# def prepString(_str, _noise=True, _multiplespaces=True):
#     noise_list = [".", ",", "?", "!", ";", ")", "~", "("]
#     # remove noise (punctuation) if asked (by default yes)
#     if _noise:
#         for car in noise_list:
#             _str = _str.replace(car, "")
#     # replace multiple spaces by ine in string if requested (default yes)
#     if _multiplespaces:
#         _str = re.sub("\s+", " ", _str).strip()
#     return _str.strip().lower()
#
#
# def hamming_distance(string1, string2):
#     if (len(string1) != len(string2)):
#         return -1
#     # Start with a distance of zero, and count up
#     distance = 0
#     # Loop over the indices of the string
#     L = len(string1)
#     for i in range(L):
#         # Add 1 to the distance if these two characters are not equal
#         if string1[i] != string2[i]:
#             distance += 1
#     # Return the final count of differences
#     return distance


# ML = list()
# ML = ['republique', 'francaise', 'carte', 'nationale', 'd\'identite', 'identity', 'card', 'nom', 'prenom']
# print(ML)
# L = list()


#
# for result in results_r:
#     L.append(prepString(str(result[1])))
#
#
# for result in results_v:
#     L.append(prepString(str(result[1])))
#
# print(L)
#
#
# with open('../data/output/test_auto.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow([str(L)])

# file_in = open('../data/output/test_auto.txt', "r")
# ML = file_in.readlines()
# file_in.close()

# file = open('../data/output/image_data.txt', 'w')
# file.write(str(L))
# file.close()