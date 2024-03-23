plik = open("bin.txt","rt")

for linia in plik:
    p = linia.strip()
    p2 = bin(int(p, 2)//2)
    p2 = p2[2:]
    
    while len(p) > len(p2):
        p2 = "0" + p2
    while len(p2) > len(p):
        p = "0" + p

    wynik = ""
    
    for i in range(len(p)):
        if p[i] == p2[i]:
            wynik += "0"
        else:
            wynik += "1"

    print(wynik)
