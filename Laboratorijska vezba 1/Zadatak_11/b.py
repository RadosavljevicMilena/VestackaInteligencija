"""proizvod, koja vraća proizvod svih elemenata u listi brojeva i svim njenim podlistama. Zabranjeno 
je korišćenje petlji i funkcije prod.
Primer: proizvod([[1, 3, 5],[2, 4, 6],[1, 2, 3]]) = 4320"""

from functools import reduce

def proizvod(lista) :
    return reduce(lambda acc,x: acc*x if type(x) == int else acc*proizvod(x),lista,1)

print(proizvod([[1, 3, 5],[2, 4, 6],[1, 2, 3]]))