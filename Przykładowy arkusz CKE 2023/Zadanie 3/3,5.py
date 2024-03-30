plik = open("liczby.txt", "rt")

def pot(a, x, M):
    if x == 0:
        return 1
    if x % 2 == 0:
        w = pot(a, x//2, M)
        return (w*w) % M
    if x % 2 == 1:
        w = pot(a, (x-1)//2, M)
        return (a*w*w) % M
    
dane = []
for linia in plik:
    rekord = linia.strip().split()
    dane.append(rekord)

wyn = 0
for t in dane:
    M = int(t[0])
    a = int(t[1])
    b = int(t[2])

    for x in range(0, M):
        if pot(a, x, M) == b:
            wyn += 1
            break
print(wyn)
    
