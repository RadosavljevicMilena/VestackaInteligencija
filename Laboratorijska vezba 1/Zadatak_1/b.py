"""poredak, koja 2 liste brojeva objedinjuje u jednu listu koja se sastoji od tuple objekata koji imaju 
tri elementa. Prvi element rezultujuće kolekcije je element prve liste, drugi je element druge liste 
a treći ima vredost ’Jeste’ ukoliko je element druge liste dva puta veći od elementa prve liste, 
odnosno ‘Nije’ ukoliko nije. Dužina liste je dimenzija duže od dve ulazne liste. N-ti tuple podatak 
rezultujuće kolekcije čine n-ti brojevi iz obe ulazne liste, gde na prvoj poziciji treba da se nađe 
manji, a na drugoj veći broj iz obe liste. 
Kraću ulaznu listu dopuniti sa kraja brojem 0, dok dužine obe liste ne budu iste. Zabranjeno je 
korišćenje petlji. 
Primer: poredak ([1, 7, 2, 4], [2, 5, 2]) = [(1, 2, 'Jeste'), (7, 5, 'Nije'), (2, 2, 'Nije'), (4, 0, 'Nije')]"""

from itertools import zip_longest

niz1=[1,2,3,4,9]
niz2 = [5,2,6,8]
def poredak(lista1, lista2):
    return list(map(lambda x: (
        min(x[0],x[1]),
        max(x[0],x[1]),
        "Jeste" if x[1] == 2 * x[0] else "Nije"
    ),
    zip_longest(lista1, lista2, fillvalue=0)))

print(poredak(niz1,niz2))