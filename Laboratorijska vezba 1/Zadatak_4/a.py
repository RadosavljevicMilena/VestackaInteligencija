#zbir, koja kreira novu listu čiji su elementi zbirovi susednih elementa liste.

def zbir(lista):
    return [lista[i] + lista[i+1] for i in range(0,len(lista)-1)]

lista1=[1,2,3,4,5]
print(zbir(lista1))