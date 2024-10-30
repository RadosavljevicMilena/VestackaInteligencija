"""zamena, koja u listi brojeva, brojeve manje od broja x, koji se prosleđuje kao argument, 
zamenjuje zbirom svih vrednosti ulazne liste, koje imaju indeks veći od indeksa broja koji se 
obrađuje. 
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi). 
Primer: zamena([1, 7, 5, 4, 9, 1, 2, 7], 5) = [35, 7, 5, 19, 9, 9, 7, 7]"""

from functools import reduce
import operator

def zamena(lista,vr) :
    return [lista[i] if lista[i] >= vr else sum(lista[i+1:]) for i in range(len(lista))]

print(zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))