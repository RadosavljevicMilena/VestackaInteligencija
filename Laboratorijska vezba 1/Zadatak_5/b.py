"""proizvod, koja računa proizvod liste podlisti (A) i liste brojeva (B). Smatrati da je broj podlisti u 
listi A jednak dužini liste B. Funkcija vraća listu koja ima onoliko elemenata koliko je dužina 
ulaznih listi. N-ti element izlatne liste predstavlja sumu svih elemenata N-te podliste liste A koji u 
prethodno pomnoženi N-tim elementom u liste B. Zabranjeno je korišćenje petlji i funkcije sum. 
Primer: proizvod([[1,2,3],[4,5,6],[7,8,9]], [1,2,3]) = [6, 30, 72]"""

from functools import reduce

def proizvod(A,B) :
   pomocna = list(map(lambda x: reduce(lambda a, b: a + b, x), A))
   #ili return  list(map(lambda x: reduce(lambda y,z: y+z,x[0])* x[1],zip(A,B))) bez pomocne
   return [pomocna[i] * B[i] for i in range(0,len(B))]


niz1 = [[1,2,3],[4,5,6],[7,8,9]]
niz2=[1,2,3]
print(proizvod(niz1, niz2))