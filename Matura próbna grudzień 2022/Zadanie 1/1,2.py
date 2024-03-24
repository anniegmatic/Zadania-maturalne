plik = open("mecz.txt", "rt")

def set(mecz):
    wynA = 0
    wynB = 0
    wyn = ""
    
    for i in range(len(mecz)):
        if mecz[i] == "A":
            wynA += 1
        else:
            wynB += 1

        if wynB >= 1000 and wynA <= wynB - 3:
            wyn = "B " + str(wynA) + ":" + str(wynB)
            return wyn
        elif wynA >= 1000 and wynB <= wynA - 3:
            wyn = "A " + str(wynA) + ":" + str(wynB)
            return wyn
            

for linia in plik:
    rekord = linia.strip()

print(set(rekord))
