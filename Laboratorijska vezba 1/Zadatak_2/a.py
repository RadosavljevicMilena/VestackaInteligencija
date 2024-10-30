#numlista, koja iz liste koja može da sadrži elemente različitog tipa izdvaja samo numeričke vrednostii

def numlista(lista) -> list[int]:
    return list(filter(lambda x: type(x) == int, lista))

lista1 = [1,2, "osam", 3,"pet", 14, "Marko"]
print(numlista(lista1))