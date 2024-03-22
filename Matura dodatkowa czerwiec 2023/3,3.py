plik = open("anagram.txt", "rt")
dane = []

def roznica(tab):
    najwieksza = 0
    for i in range(len(tab)-1):
        x = abs(int(tab[i],2) - int(tab[i+1],2))
        if x > najwieksza:
            najwieksza = x
    najwieksza = str(bin(najwieksza))
    najwieksza = najwieksza[2:]
    
    return najwieksza

            
for linia in plik:
    rekord = linia.strip()
    dane.append(rekord)


print(roznica(dane))

    
