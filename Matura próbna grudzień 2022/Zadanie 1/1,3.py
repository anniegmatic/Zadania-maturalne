plik = open("mecz.txt", "rt")

def passa(mecz):
    pasA = 1
    maxpasA = 0
    pasB = 1
    maxpasB = 0
    dA = 0
    dB = 0
    
    for i in range(len(mecz)-1):
        if mecz[i] == "A":
            pasB = 1
            if mecz[i+1] == "A":
                pasA +=1
                if pasA >= 10 and pasA > maxpasA:
                    maxpasA = pasA
            if pasA >= 10 and mecz[i+1] == "B":
                    dA += 1
                    
        elif mecz[i] == "B":
            pasA = 1
            if mecz[i+1] == "B":
                pasB +=1
                if pasB >= 10 and pasB > maxpasB:
                    maxpasB = pasB
            if pasB >= 10 and mecz[i+1] == "A":
                    dB += 1
                    
    wyn = str(dA + dB)
    if maxpasA > maxpasB:
        wyn += " A " + str(maxpasA)
    else:
        wyn += " B " + str(maxpasB)
        
    return wyn
        

for linia in plik:
    rekord = linia.strip()

print(passa(rekord))
