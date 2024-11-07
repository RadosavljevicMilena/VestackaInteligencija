"""Korišdenjem programskog jezika Python, napisati funkciju zamena, koja u listi brojeva, brojeve manje od broja 
x, koji se prosleđuje kao argument, zamenjuje zbirom svih vrednosti ulazne liste, koje imaju indeks vedi od 
indeksa broja koji se obrađuje. Zabranjeno je korišdenje petlji (osim u comprehension sintaksi). 
Primer: zamena([1, 7, 5, 4, 9, 1, 2, 7], 5) = [35, 7, 5, 19, 9, 9, 7, 7] """

from functools import reduce
def zamena(lista, vr) :
    return [lista[index] if lista[index] >=vr else reduce(lambda x,y:x+y,lista[index+1:],0) for index in range(len(lista))]

print(zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))