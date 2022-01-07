import easyocr
import cv2
import spacy as sp
import nltk
from nltk.corpus import stopwords

nlp = sp.load("fr_core_news_sm")


def return_POS(sentence):
    doc = nlp(sentence)
    return [(X, X.pos_) for X in doc]


img = cv2.imread('../data/ci1-verso.png', 0)
reader = easyocr.Reader(['fr'])
results = reader.readtext(img)
test = ""
for result in results:
    test += result[1] + " "

print(test)
print(return_POS(test))







# test = "Brandy est un fille un peu belle mais elle ne le sait pas croyant qu'elle est tres belle. Samson a tout dit."
# nltk.download()
# stopWords = set(stopwords.words('french'))
# print(stopWords)


#
# def return_token(sentence):
#     doc = nlp(sentence)
#     return [X.text for X in doc]
#
#
# clean_words = []
# for token in return_token(test):
#     if token not in stopWords:
#         clean_words.append(token)
#
# print(clean_words)

# for r in results:
#     print(r[0])
#     for rr in r[0]:
#         print(rr[0])
#         print(rr[1])
#     print(r[1])
#     print(r[2])
#
# print(results[1])