"""izmeni, koja svaki n-ti element liste zamenjuje brojem koji predstavlja sumu svih elemenata originalne liste, od prvog, do n-tog elementa. 
Primer: izmeni([1, 2, 4, 7, 9]) = [1, 3, 7, 14, 23]"""

from itertools import *

def izmeni(lista) : 
    return list(accumulate(lista, lambda x,y:x+y))

print(izmeni([1, 2, 4, 7, 9]))