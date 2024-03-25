plik = open("liczby.txt","rt")

def odbicie(tab):
    wyn = []
    for x in tab:
        x = int(x[::-1])
        if x % 17 == 0:
            wyn.append(x)
    return wyn

tab = []
for linia in plik:
    rekord = linia.strip()
    tab.append(rekord)

print(odbicie(tab))
