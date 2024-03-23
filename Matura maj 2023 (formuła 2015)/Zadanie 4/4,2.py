plik = open("slowa.txt", "rt")

def wakacje(tab):
    wynik = ""
    for x in tab:
        wakajki = 0

        xw = x.count("w")
        xa = x.count("a")
        xk = x.count("k")
        xc = x.count("c")
        xj = x.count("j")
        xe = x.count("e")
        
        while xw > 0 and xa > 1 and xk > 0 and xc > 0 and xj > 0 and xe > 0:
            wakajki += 1
            xw -= 1
            xa -= 2
            xk -= 1
            xc -= 1
            xj -= 1
            xe -= 1

        wynik += str(wakajki) + " "

    return wynik

tab = []

for linia in plik:
    rekord = linia.strip()
    tab.append(rekord)
    
print(wakacje(tab))

