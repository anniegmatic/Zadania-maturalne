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


'''
2^0 1 - 1
2^1 2 - 2 3
2^2 4 - 4 5 6 7
2^3 8 - 8 9 10 11 12 13 14 15
2^4 16 - 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
2^5 32
'''
