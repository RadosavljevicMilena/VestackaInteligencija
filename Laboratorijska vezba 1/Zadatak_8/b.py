"""izracunaj, koja u listi koja može da se sastoji od brojeva i podlisti, na n-tom mestu u rezultujućem 
nizu upisuje broj sa n-te pozicije iz ulaznog niza, a ukoliko se radi o podlisti, zamenjuje je 
proizvodom svih brojeva u podlisti. 
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi). 
Primer: izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]) = [1, 5, 15, 8, 2, 18] """

from functools import reduce

def izracunaj(lista) :
    return [x if not type(x)==list else reduce(lambda y,z: y*z, x) for x in lista]

print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))