plik = open("liczby.txt", "rt")

def tesame(tab):
    licz = 0
    wyn = []
    wyn2 = ""
    for x in tab:
        if x[0] == x[-1]:
            licz += 1
            wyn.append(x)
    wyn2 = str(licz) + " " +  str(wyn[0])
    return wyn2

tab2 =[]
for linia in plik:
    rekord = linia.strip()
    tab2.append(rekord)

print(tesame(tab2))
