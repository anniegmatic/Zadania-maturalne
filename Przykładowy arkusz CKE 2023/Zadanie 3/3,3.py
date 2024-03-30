plik = open("liczby.txt", "rt")

def pierwsza(a):
    a = int(a)
    if a <= 1:
        return 0
    for i in range(2, a):
        if a % i == 0:
            return 0
    return 1

licz = 0
for linia in plik:
    rekord = linia.strip().split()
    if pierwsza(rekord[0]) == 1:
        licz += 1

print(licz)
