plik = open("pary.txt", "rt")

def pary(tab):
    x = int(tab[0])
    y = int(tab[1]) # większa liczba
    
    while x < y:
        y = y // 2
    if x == y:
        return 1
    return 0
        
        
for linia in plik:
    rekord = linia.strip().split()
    if pary(rekord) == 1:
        print(linia.strip())
