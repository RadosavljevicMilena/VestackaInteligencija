"""izdvoji, koja iz zadate liste čiji su elementi liste, izdvaja n-ti element i formira rezultujuću listu, pri 
čemu je n=0 za prvu podlistu i uvećava se sukcesivno za 1. Ukoliko ne postoji n-ti element u listi 
vraća se 0. 
Primer: izdvoji([5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]) = [5, 9, 0, 12]"""

def izdvoji(lista) :
    return [podlista[i] if i < len(podlista) else 0 for i, podlista in zip(range(len(lista)), lista)]

print(izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))