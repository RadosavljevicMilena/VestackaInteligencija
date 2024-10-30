"""suma, koja formira novu listu tako što nalazi sumu svih elemenata u podlistama. Zabranjeno je 
korišćenje petlji i funkcije sum. 
Primer: suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) = [6, 15, 24] """

from functools import reduce
def suma(lista) :
    return list(map(lambda p: reduce(lambda x,y : x+y,p), lista))

print(suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))