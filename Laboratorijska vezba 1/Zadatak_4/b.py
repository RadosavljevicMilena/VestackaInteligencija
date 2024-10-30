"""suma, koja vraća sumu svih elemenata u listi brojeva i svim njenim podlistama. Zabranjeno je 
korišćenje petlji i funkcije sum. 
Primer: suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) = 45"""

from functools import reduce
from itertools import *

def suma(lst) :
    return lst if type(lst)==int else suma(lst[0]) + suma(lst[1:]) if lst else 0

lista1=[1,[2,3],[4,5],6]
print(suma(lista1))

