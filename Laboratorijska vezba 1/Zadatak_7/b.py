"""objedini, koja od liste tuple objekata kreira dictionary. Prvi element svakog tuple objekta postaje 
ključ rečnika, dok sve ostale vrednosti postaju vrednost (lista vrednosti). 
Ukoliko tuple podatak ima manje od 2 vrednosti, na mesto vrednosti postaviti None. 
Ukoliko ključ već postoji u rečniku, prepisati njegovu vrednost novom. 
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi). 
Primer: objedini([(1), (3, 4, 5), (7), (1, 4, 5), (6, 2, 1, 3)]) = { 1: [4, 5], 3: [4, 5], 7: None, 6: [2, 1, 3] }"""


def objedini(lista):
    return { x[0]: list(x[1:]) if len(x)>1 else "None" for x in lista}

print(objedini([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)]))