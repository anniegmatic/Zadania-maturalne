plik = open("bin.txt","rt")

najwieksza = 0
najwiekszab = ""

for linia in plik:
    rekord =linia.strip()
    
    if int(rekord, 2) > najwieksza:
        najwieksza = int(rekord, 2)
        najwiekzab = rekord

print(najwiekzab)
