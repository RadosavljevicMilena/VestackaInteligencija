#izmeni, koja kreira novu listu tako da elemente na parnim pozicijama uvećava za jedan, dok 
#elemente na neparnim pozicijama umanjuje za 1.
#Primer: izmeni([8, 5, 3, 1, 1]) = [9, 4, 4, 0, 2]

def izmeni(lista1) :
    return [lista1[i]+1 if i%2 == 0 else lista1[i]-1 for i in range(len(lista1))]

print(izmeni([8, 5, 3, 1, 1]))