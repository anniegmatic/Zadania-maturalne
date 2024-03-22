plik = open("anagram.txt", "rt")
dane = []


def anagramy(tab):
    selekcja = []
    for x in tab:
        if x[0] == "1" and len(x) == 8:
            selekcja.append(x)

    wyniki = []
    for x in selekcja:
        jedynki = x.count("1")
        # najwięcej anagramów jest jak równowaga jedynek i zer jest zachowana (4:4)
        # lub jak jest jedna więcej jedynka (bo od jedynki się zaczyna) (5:3)
        if jedynki == 4 or jedynki == 5:
            wyniki.append(x)

    return wyniki

            
for linia in plik:
    rekord = linia.strip()
    dane.append(rekord)


print(anagramy(dane))

    
