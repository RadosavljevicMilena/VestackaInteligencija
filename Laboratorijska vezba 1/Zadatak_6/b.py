"""objedini, koja 2 liste brojeva objedinjuje u jednu listu koja se sastoji od parova brojeva (tuple). 
Dužina liste treba da je dimenzija duže od dve ulazne liste. N-ti tuple podatak rezultujuće 
kolekcije čine n-ti brojevi iz obe ulazne liste, gde na prvoj poziciji treba da se nađe manji, a na 
drugoj veći broj iz obe liste. 
Kraću ulaznu listu dopuniti sa kraja brojem 0, dok dužine obe liste ne budu iste. 
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi). 
Primer: objedini([1, 7, 2, 4, 5], [2, 5, 2]) = [(1, 2), (5, 7), (2, 2), (0, 4), (0, 5)]"""

from itertools import zip_longest

def objedini(lista1, lista2) :
    return list(map(lambda x: (min(x[0],x[1]), max(x[0],x[1])),zip_longest(lista1,lista2,fillvalue=0)))

niz1=[1,2,3,4]
niz2=[5,6,1,2]

print(objedini(niz1,niz2))