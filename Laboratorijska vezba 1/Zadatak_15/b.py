"""promeni, koja u listi brojeva, brojeve veće ili jednake broju x, koji se prosleđuje kao argument, 
umanjuje za x, dok brojeve manje od x uvećava za x 
Primer: promeni([7, 1, 3, 5, 6, 2], 3) = [4, 4, 0, 2, 3, 5]"""

def promeni(lista,x) :
    return [y-x if y >=x else y+x for y in lista]

print(promeni([7, 1, 3, 5, 6, 2], 3))