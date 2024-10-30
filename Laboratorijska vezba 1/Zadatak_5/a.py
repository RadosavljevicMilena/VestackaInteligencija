#brojel, koja broji koliko elemenata ima svaka podlista liste koja joj je prosleđena. Ukoliko 
#elemenat liste nije podlista funkcija vraća -1.
#Primer: brojel([1, 2], [3, 4, 5], 'el', ['1', 1]) = [2, 3, -1, 2] 

def brojel(lista) :
    return (list(map(lambda x: len(x) if type(x) == list else -1, lista)))

lista1= [1,[2,3,4,1,4], "el", [2,4,3]]
print(brojel(lista1))