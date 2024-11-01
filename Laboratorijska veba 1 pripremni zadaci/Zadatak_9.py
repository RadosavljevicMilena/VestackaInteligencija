"""Korišdenjem programskog jezika Python, napisati funkciju prosek, koja za svaki element
prosleđene liste, koja se sastoji isključivo od podlisti, vrada aritmetičku sredinu svih njenih
vrednosti.
Primer: prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]) =
 [3.25, 4.75, 4.0, 5.0]"""

from functools import reduce

def prosek(lista) : 
    return list(map(lambda x: reduce(lambda t,r : t+r, x)/len(x), lista))

print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))