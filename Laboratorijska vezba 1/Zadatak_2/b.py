"""spojidict, koja 2 liste obejkata objedinjuje u listu sa elementima tipa dictionary. Dužina liste je 
dimenzija duže od dve ulazne liste. N-ti dictionary element rezultujuće kolekcije čine n-ti objekti 
iz obe ulazne liste, gde se na prvoj poziciji nalazi element prve liste uparen sa ključem 'prvi', a 
na drugoj poziciji element druge liste uparen sa ključem 'drugi'. Kraću ulaznu listu dopuniti sa 
' - ', dok dužine obe liste ne budu iste. Zabranjeno je korišćenje petlji."""

from itertools import zip_longest

def spojdict(lista1,lista2):
    return list(map(lambda x:({"prvi": x[0], "drugi":x[1]}),zip_longest(lista1, lista2,fillvalue="-")))

listaa1 = [1,2,3,4]
listaa2 = [6,7,8,9]

print(spojdict(listaa1, listaa2))