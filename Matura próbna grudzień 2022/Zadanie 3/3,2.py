plik = open("liczby.txt", "rt")

def pierwsza(x):
    if x <= 1:
        return 0
    for i in range(2, x):
        if x % i == 0:
            return 0
    return 1
            
suma = 0
for linia in plik:
    rekord = linia.strip()
    suma += pierwsza(int(rekord)-1)

print(suma)
