#parni, koja određuje broj parnih elemenata zadate liste. 
#Primer: parni([1, 7, 2, 4, 5]) = 2 

def parni(lista:list[int])->int:
    return len(list(filter(lambda x: x%2==0, lista)))
niz=[1,2,4,3]
print(parni(niz))