plik = open("anagram.txt", "rt")
dane = []

def bezzera(tab):
    ilosc = 0
    for x in tab:
        x = str(x)
        if "0" not in x:
            ilosc += 1
    return ilosc

def suma(tab):
    rozne = 0
    wynik = 0

    for x in tab:
        cyfry = ["0","1","2","3","4","5","6","7","8","9"]
        suma = 0
        for y in str(x):
            if str(y) in cyfry:
                cyfry.remove(str(y))
        for i in range(10):
            if str(i) not in cyfry:
                suma += int(i)
        if suma > rozne:
            rozne = suma
            wynik = x
            
    return wynik
    
for linia in plik:
    rekord = linia.strip()
    dane.append(int(rekord,2))


print("a)", bezzera(dane))
print("b)", suma(dane))

    
