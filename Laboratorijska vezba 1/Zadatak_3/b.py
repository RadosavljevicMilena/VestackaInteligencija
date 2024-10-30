"""spoji, koja 2 liste brojeva objedinjuje u jednu listu koja se sastoji od tuple objekata koji imaju tri 
elementa. Prvi element rezultujuće kolekcije je element prve liste, drugi je element druge liste a 
treći je zbir elemenata. Dužina liste je dimenzija duže od dve ulazne liste. N-ti tuple podatak 
rezultujuće kolekcije čine n-ti brojevi iz obe ulazne liste, gde na prvoj poziciji treba da se nađe 
manji, a na drugoj veći broj iz obe liste. 
Kraću ulaznu listu dopuniti sa kraja brojem 0, dok dužine obe liste ne budu iste. Zabranjeno je 
korišćenje petlji. """
from itertools import zip_longest

def spoji(lista1, lista2):
    return(list(map(lambda x: (min(x[0],x[1]),max(x[0],x[1]), x[0]+x[1]), zip_longest(lista1,lista2,fillvalue=0))))

lista11 = [1,2,3]
lista22= [5,6,7,8]

print(spoji(lista11,lista22))