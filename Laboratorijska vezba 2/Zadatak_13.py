"""Korišdenjem programskog jezika Python, napisati funkciju skupi, koja kreira novu listu tako da svaka dva 
susedna elementa liste ciji su elementi iskljucivo podliste zamenjuje podlistom koja sadrži zbir elemeata na 
odgovarajudim pozicijama. Elemente koji nedostaju tretirati kao nule. Zabranjeno je korišdenje petlji (osim u 
comprehension sintaksi). 
Primer: skupi([[1, 3, 5], [2, 4, 6], [1, 2]]) = [[3, 7, 11], [3, 6, 6]] """

from itertools import *

def skupi(lista) :
    return [[a+b for a,b in zip_longest(x[0], x[1], fillvalue=0)] for x in pairwise(lista)]

print(skupi([[1, 3, 5], [2, 4, 6], [1, 2]]))
