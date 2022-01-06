import locale
from functools import cmp_to_key


class Compfr(object):
    """comparaison de 2 chaines selon le dictionnaire français"""

    def __init__(self, decod='utf-8'):
        self.decod = decod
        self.loc = locale.getlocale()  # stocker la locale courante
        self.espinsec = u'\xA0'  # espace insécable

    def __call__(self, v1, v2):

        # on convertit en unicode si nécessaire
        if isinstance(v1, str):
            v1 = v1.decode(self.decod)
        if isinstance(v2, str):
            v2 = v2.decode(self.decod)

        # on retire les tirets et les blancs insécables
        v1 = v1.replace(u'-', u'')
        v1 = v1.replace(self.espinsec, u'')
        v2 = v2.replace(u'-', '')
        v2 = v2.replace(self.espinsec, u'')

        locale.setlocale(locale.LC_ALL, '')
        comp = locale.strcoll(v1, v2)
        locale.setlocale(locale.LC_ALL, self.loc)  # retour à la locale courante

        return comp  # retour du résultat de la comparaison


L = ['pèche', 'PÈCHE', 'pêche', 'PÊCHE', 'péché', 'PÉCHÉ', 'pécher', 'pêcher']

compfr = Compfr()
L.sort(key=cmp_to_key(compfr))
for mot in L:
    print(mot)