#izbroj, koja određuje broj elemenata liste, gde svaki element može da bude podlista ili broj. 
#Zabranjeno je korišćenje petlji (osim u comprehension sintaksi).
#Primer: izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]) = 13

from functools import reduce
def izbroj(lista) :
    return reduce(lambda acc,x: acc+1 if type(x) == int else acc+izbroj(x),lista,0)

print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))
