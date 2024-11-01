"""Korišdenjem programskog jezika Python, napisati funkciju uredi, koja svaki od prvih N
elemenata uvedava za definisanu vrednost a preostale umanjuje za definisanu vrednost.
Funkciji se prosleđuje lista koja sadrži samo numeričke vrednosti i vrednost koja treba da
se uvedava, odnosno umanjuje.
Primer: uredi([1, 2, 3, 4, 5], 3, 1) = [2, 3, 4, 3, 4]"""

from itertools import zip_longest

def uredi(lista, N, vr) :
    return [lista[i] + vr if i < N else lista[i] - vr for i in range(len(lista))]

print(uredi([1, 2, 3, 4, 5], 3, 1))