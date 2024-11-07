"""Korišdenjem programskog jezika Python, napisati funkciju saberi, koja listu tuple vrednosti
transformiše u listu brojeva, koji se dobijaju primenom operacije sabiranja.
Primer: operacija([(1, 4, 6), (2, 4), (4, 1)]) = [11, 6, 5]"""

from functools import reduce

def saberi(lista) :
    return list(map(lambda z : reduce(lambda x,y: x+y, z), lista))

print(saberi([(1, 4, 6), (2, 4), (4, 1)]))