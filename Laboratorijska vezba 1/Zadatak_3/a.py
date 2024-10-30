#uredi, koja svaki od prvih n elemenata uvećava za definisanu vrednost a preostale umanjuje za definisanu vrednost.
#  Funkciji se prosleđuje lista koja sadrži samo numeričke vrednosti i vrednost 
# koja treba da se uvećava, odnosno umanjuje. Zabranjeno je korišćenje petlji.

def uredi(lista, vrednost, n) :
    return [lista[i] + (vrednost if i<n else -vrednost) for i in range(0, len(lista))]

print(uredi([1, 2, 3, 4, 5], 1,3))