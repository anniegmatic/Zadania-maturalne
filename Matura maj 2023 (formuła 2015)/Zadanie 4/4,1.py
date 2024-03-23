plik = open("slowa.txt", "rt")

def WK(tab):
    tab2 = []
    for x in tab:
         if x.count("w") == x.count("k"):
             tab2.append(x)
    return tab2

tab = []

for linia in plik:
    rekord = linia.strip()
    tab.append(rekord)

for x in WK(tab):
    print(x)
