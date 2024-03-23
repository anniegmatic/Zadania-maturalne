plik = open("bin.txt","rt")

def bloki(znaki):
    b = 1
    for i in range(len(znaki)-1):
        if znaki[i] != znaki[i+1]:
            b += 1
    return b

ile = 0
for linia in plik:
    rekord =linia.strip()
    if bloki(rekord) <= 2:
        ile +=1

print(ile)
