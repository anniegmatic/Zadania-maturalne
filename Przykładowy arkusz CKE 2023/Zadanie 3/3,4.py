plik = open("liczby.txt", "rt")

def dzielniki(a):
    tab = []
    a = int(a)
    if a <= 1:
        tab = [1]
    for i in range(1, a+1):
        if a % i == 0:
            tab.append(i)
    return tab

wyn = 0
for linia in plik:
    licz = 0
    rekord = linia.strip().split()
    M = rekord[0]
    a = rekord[1]
    b = rekord[2]

    for x in dzielniki(a):
        if x in dzielniki(M):
            licz += 1

    if licz == 1:
        wyn +=1

print(wyn)
