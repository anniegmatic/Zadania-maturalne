plik = open("liczby.txt","rt")

def pierwsza(a):
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def odbicie(tab):
    wyn = []
    for x in tab:
        odb = int(x[::-1])
        if pierwsza(int(x)) == True and pierwsza(odb) == True:
            wyn.append(int(x))
    return wyn

tab = []
for linia in plik:
    rekord = linia.strip()
    tab.append(rekord)

print(odbicie(tab))
