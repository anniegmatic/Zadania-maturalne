plik = open("liczby.txt", "rt")

def sito(n):
    tab = [1] * (n+1)
    tab[1] = tab[0] = 0
    
    for i in range(2, n+1):
        if tab[i] == 1:
            j = i*i
            while j <= n:
                tab[j] = 0
                j += i
    return tab

pierwsze = sito(1000000)
maxx = 0
minn = 100000000
maxxlicz = 0
minnlicz = 0

for linia in plik:
    rekord = linia.strip()
    rekord = int(rekord)
    x = 2
    y = rekord - x
    ile = 0
    
    while x <= y:
        if pierwsze[x] == 1 and pierwsze[y] == 1:
            ile += 1
        x += 1
        y = rekord - x
    if ile > maxx:
        maxx = ile
        maxxlicz = rekord
    if ile < minn:
        minn = ile
        minnlicz = rekord

print(maxxlicz, maxx)
print(minnlicz, minn)
