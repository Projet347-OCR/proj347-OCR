from easygui import *


def envoyer(cadeau):
    print("Lui envoyer", cadeau)


message = "Que dit-elle ?"
title = "Declaration"
if boolbox(message, title, ("Elle m_aime", "Elle ne m_aime pas")):
        envoyer("Fleurs")
else:
    pass
