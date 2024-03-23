plik = open("slowa.txt", "rt")

def wakacyjne(tab):
    wynik = ""
    
    for x in tab:
        wykreslenia = [len(x)]
        lista = ["w","a","k","a","c","j","e"]
        j = 0
        wyciete = 0
        
        for i in range(len(x)):
            if x[i] == lista[j]:
                if j == len(lista) - 1:
                    wykreslenia.append(len(x) - i - 1 + wyciete)
                    j = -1
                j += 1
            else:
                wyciete += 1

        wynik += str(min(wykreslenia)) + " "

    return wynik
                
tab = []

for linia in plik:
    rekord = linia.strip()
    tab.append(rekord)
    
print(wakacyjne(tab))

