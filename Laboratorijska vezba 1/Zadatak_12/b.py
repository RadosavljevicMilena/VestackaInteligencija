"""izracunaj, koja u listi koja se sastoji od brojeva i podlisti, menja svaki broj njegovim kvadratom, 
dok listu zamenjuje zbirom kvadrata brojeva koji je čine.  
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi). 
Primer: izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]) = [4, 16, 14, 20, 4, 106]"""

from functools import reduce

def izracunaj(lista1) :
    return [x*x if type(x) == int else reduce(lambda u,y: u+y*y,x,0) for x in lista1]

print(izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]))