plik = open("liczby.txt","rt")

def odbicie(tab):
    maxx = 0
    for i in range(len(tab)):
        odb = int(tab[i][::-1])
        if abs(int(tab[i]) - odb) > maxx:
            maxx = abs(int(tab[i]) - odb)
            wyn = []
            wyn.append(int(tab[i]))
            wyn.append(abs(int(tab[i]) - odb))
    return wyn

tab = []
for linia in plik:
    rekord = linia.strip()
    tab.append(rekord)

print(odbicie(tab))
