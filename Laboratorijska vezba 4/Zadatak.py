"""3. Igra pogađanja brojeva zahteva od igrača da pogodi zamišljeni dvanaestocifreni broj. Igrač u
svakom koraku bira jednu od 10 cifara, nakon čega mu se otkrivaju sve pozicije u broju na kojima
se ta cifra nalazi. Odrediti i zapamtiti redosled izbora cifara koji vodi rešenju sa manje od 10
pokušaja (smatrati da dvaneastocifreni broj u svom zapisu nikada nema svih 10 cifara).
2 7 1 8 0 4 8 5 3 4 2 8"""

#heuristika je da nam treba 12 pokusaja (znaci ovde se radi o broju pozicija koje su ostale neotkrivene i nema veze sa time sto nam je jednocifreni broj)
# , odnosno da imamo sve razlicite cifre, a g je stvaran broj pokusaja

def a_star_guess(number):
    # Ciljni broj - pretvaranje u listu
    goal = [int(digit) for digit in str(number)]

    # Početne vrednosti
    open_set = []  # Lista za obradu
    closed_set = set()  # Obrađeni čvorovi
    prev_nodes = {}  # Praćenje prethodnika
    g = {}  # Cena puta
    path = []  # Redosled pogodaka

    # Početno stanje
    start = tuple(['_'] * 12)  # Početni broj sa nepoznatim ciframa
    g[start] = 0
    open_set.append(start)  # Dodaj početno stanje, lista tuple koja sadrži sva stanja kroz koja smo prošli
    prev_nodes[start] = None

    # Funkcija heuristike: broj nepoznatih cifara
    def h_function(state):
        return sum(1 for x in state if x == '_')

    while open_set:
        # Pronađi čvor sa najmanjom vrednošću f(n) = g(n) + h(n)
        #key definiše po kom kriterijumu funkcija min traži najmanju vrednost
        #Kombinuje dve vrednosti:
        #g[state]: Cena puta od početnog stanja do trenutnog stanja (state).
        #h_function(state): Heuristika, procena koliko još treba do cilja iz trenutnog stanja.
        current = min(open_set, key=lambda state: g[state] + h_function(state))
        open_set.remove(current)

        # Ako smo dostigli ciljno stanje
        if list(current) == [str(digit) for digit in goal]:
            # Rekonstruiši put
            while current is not None:
                path.append(current)
                #korak unazad i zato ide reverse
                current = prev_nodes[current]
            path.reverse()
            return path

        closed_set.add(current)

        # Iteracija kroz sve moguće cifre (0-9)
        for guess in range(10):
            guess = str(guess)
            #Za pocetak, kopiramo trenutno stanje dokle smo dosli
            next_state = list(current)
            #Sluzi da vidimo da li ta cifra koju cemo da probamo uopste postoji
            updated = False

            # Ažuriranje stanja na osnovu pogođenih pozicija
            for i in range(12):
                if goal[i] == int(guess) and current[i] == '_':
                    next_state[i] = guess
                    updated = True

            if not updated:
                continue

            next_state = tuple(next_state)

            # Ako je stanje već obrađeno, preskoči. Ako pokusamo 2 puta istu cifru
            if next_state in closed_set:
                continue

            # Računanje cene puta
            tentative_g = g[current] + 1 #koliko smo do sada imali pokusaja + ovaj poslednji
            if next_state not in open_set or tentative_g < g.get(next_state):
                prev_nodes[next_state] = current
                g[next_state] = tentative_g
                if next_state not in open_set:
                    open_set.append(next_state)

    # Ako se algoritam završi bez rešenja
    return path


path = a_star_guess(271804853428)
print("Koraci do rešenja:")
for step in path:
    print("Medjuresenje:")
    print(step)
