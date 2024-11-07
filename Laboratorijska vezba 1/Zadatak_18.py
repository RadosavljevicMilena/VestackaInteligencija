"""Korišdenjem programskog jezika Python, napisati funkciju kreiraj, koja na osnovu ulazne
liste čiji su elementi podliste, kreira listu u kojoj svaki element rezultujude liste predstavlja
podlistu koja je razlika susednih podlisti ulazne liste.
Primer: kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]) = [[1, 3], [2], [4, 6, 7]]"""

def kreiraj(lista) : 
    return [[x for x in lista[i] if x not in lista[i + 1]] for i in range(len(lista) - 1)]

print(kreiraj([[1, 2, 3], [2, 4, 5], [4, 5, 6, 7], [1, 5]]))