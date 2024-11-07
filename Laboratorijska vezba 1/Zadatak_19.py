"""Korišdenjem programskog jezika Python, napisati funkciju stepenuj, koja listu tuple
vrednosti transformiše u listu brojeva, koji se dobijaju primenom operacije stepenovanja,
tako što se prvi element stepenuje drugim, zatim se rezultat stepenuje tredim sve dok se
ne dođe do poslednjeg elementa u tuple-u.
Primer: stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]) = [1, 32, 256, 5]"""

from functools import reduce

def stepenuj(lista) :
    return list(map(lambda x: reduce(lambda y,t : y**t, x),lista))

print(stepenuj([(1, 4, 2), (2, 5, 1), (2, 2, 2, 2), (5, )]))