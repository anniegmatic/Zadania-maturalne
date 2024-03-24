plik = open("mecz.txt", "rt")

def rozne(mecz):
    wynik = 0
    
    for i in range(1, len(mecz)):
        if mecz[i] != mecz[i-1]:
            wynik += 1
            
    return wynik

for linia in plik:
    rekord = linia.strip()
    print(rekord)
    print(len(rekord))
print(rozne(rekord))
