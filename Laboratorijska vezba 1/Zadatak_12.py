"""Korišdenjem programskog jezika Python, napisati funkciju presek, koja prihvata dve liste
(bilo kog tipa podataka), a ima povratnu vrednost koja je lista sastavljena od svih
elemenata koji se nalaze u obe liste.
Primer: presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]) = [1, "1"]"""

def presek(lista1, lista2) :
    return list(filter(lambda x:x in lista1,lista2))

print(presek([5, 4, "1", "8", 3, 7, 1], [1, 9, "1"]))