"""suma, koja vraća sumu svih elemenata u listi brojeva i svim njenim podlistama. Zabranjeno je 
korišćenje petlji i funkcije sum. 
Primer: suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) = 45"""

from functools import reduce

def suma(lista) :
    return reduce(lambda acc, x : acc+x if type(x) == int else acc+suma(x), lista, 0)

print(suma(suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]])))

