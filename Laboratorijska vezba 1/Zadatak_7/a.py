"""operacija, koja listu tuple vrednosti transformiše u listu brojeva, koji se dobijaju primenom 
operacije prosleđene putem argumenta.
Primer: operacija([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y) = [11, 6, 5]"""

from functools import reduce

def operacija(lista,op) :
    return list(map(lambda x: reduce(op,x),lista))

print(operacija([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y))