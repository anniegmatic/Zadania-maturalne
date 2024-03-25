plik = open("liczby.txt","rt")

def licz(tab):
    powt1, powt2, powt3 = 0, 0, 0
    tab2 = tab.copy()
    for x in tab:
        powt = tab2.count(x)

        if powt == 1:
            powt1 += 1
        elif powt == 2:
            powt2 += 1
        elif powt == 3:
            powt3 += 1

        while x in tab2:
            tab2.remove(x)
            
    wyn = str(powt1+powt2+powt3) +" " + str(powt2) + " " +str(powt3)
    return wyn
                

tab = []
for linia in plik:
    rekord = linia.strip()
    tab.append(rekord)

print(licz(tab))
