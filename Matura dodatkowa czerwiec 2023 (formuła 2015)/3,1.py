plik = open("anagram.txt", "rt")
dane = []

def rowno(tab):
    rownowaga = 0
    pr_rownowaga = 0
    
    for x in tab:
        licz0 = 0
        licz1 = 0
        for y in x:
            if y == "1":
                licz1 += 1
            else:
                licz0 += 1

        if licz1 == licz0:
            rownowaga += 1
        elif licz1 - licz0 == 1 or licz0 - licz1 == 1:
            pr_rownowaga += 1

    return rownowaga, pr_rownowaga
            

for linia in plik:
    rekord = linia.strip()
    dane.append(rekord)


print(rowno(dane))

    
