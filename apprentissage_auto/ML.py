# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import Imputer
# from sklearn.preprocessing import LabelEncoder
#
#
# dataset = open('../data/output/image_data.txt', 'r')
# X = dataset.iloc[<range of rows and input columns>].values
# y=dataset.iloc[<range of rows and output column>].values
#
# imputer=Imputer(missing_values="NaN", strategy="mean", axis=0)
# imputer=imputer.fit(X[<range of rows and columns>])
# X[<range of rows and columns>]=imputer.transform(X[<range of rows and columns>])
#
# le_X=LabelEncoder()
# X[<range of rows and columns>]=le_X.fit_transform(X[<range of rows and columns>])
# labelencoder_y = LabelEncoder()
# y = labelencoder_y.fit_transform(y)
# from sklearn.preprocessing import OneHotEncoder
# oneHE=OneHotEncoder(categorical_features=[<range of rows and columns>])
# X=oneHE.fit_transform(X).toarray()


# noise_list = [".", ",", "?", "!", ";"]


# Comparaison a l_ancienne
import re

def prepString(_str, _noise=True, _multiplespaces=True):
    noise_list = [".", ",", "?", "!", ";"]
    # remove noise (punctuation) if asked (by default yes)
    if _noise:
        for car in noise_list:
            _str = _str.replace(car, "")
    # replace multiple spaces by ine in string if requested (default yes)
    if _multiplespaces:
        _str = re.sub("\s+", " ", _str).strip()
    return _str.strip().lower()


def compareString(Str1, Str2):
    f = prepString(Str1)
    g = prepString(Str2)
    print(f)
    print(g)
    return f == g


a = compareString("Ben  oit.,", "BEN oit")
print(a)


# comparaison Hamming
def hamming_distance(string1, string2):
    if (len(string1) != len(string2)):
        return -1
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
    # Return the final count of differences
    return distance


b = hamming_distance("SAMSON", "SAMSON")
print(b)


#Jaro - Comparaison Jaro-Winkler
import jaro
c = jaro.jaro_metric("SAMSON", "SAMSON")
print(c)

d = jaro.jaro_winkler_metric("SAMSON", "SAMSON")
print(d)

# Leveinshtein
import Levenshtein as lev


def levCalclulate(str1, str2):
    Distance = lev.distance(str1, str2)
    Ratio = lev.ratio(str1, str2)
    print("Levenshtein entre {0} et {1}".format(str1, str2))
    print("> Distance: {0}\n> Ratio: {1}\n".format(Distance, Ratio))


levCalclulate("Benoit", "Ben")
levCalclulate("Benoit", "Benoist")
levCalclulate("SAMSON", "samson")


# Lien et appartenance (ratio) - Fuzzywuzzy
from rapidfuzz import fuzz

Str1 = "carte nationale d'identite / identity card"
Str2 = "carte"
Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower())
print(Partial_Ratio)


# Inversions dans la chaine (Token_Sort_Ratio)
Str1 = "Ceci est un test"
Str2 = "un test est ceci"
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower())
Token_Sort_Ratio = fuzz.token_sort_ratio(Str1,Str2)
print(Ratio)
print(Partial_Ratio)
print(Token_Sort_Ratio)
print('\n')

# Chaines de taille differentes (Cf. token_set_ratio)
Str1 = "Ce soir on regarde un match France contre Angleterre"
Str2 = "France vs Angleterre"
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
Partial_Ratio = fuzz.partial_ratio(Str1.lower(),Str2.lower())
Token_Sort_Ratio = fuzz.token_sort_ratio(Str1,Str2)
Token_Set_Ratio = fuzz.token_set_ratio(Str1,Str2)
print(Ratio)
print(Partial_Ratio)
print(Token_Sort_Ratio)
print(Token_Set_Ratio)

