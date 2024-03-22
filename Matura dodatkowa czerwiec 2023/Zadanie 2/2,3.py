def czy_mniejszy(n,s,k1,k2):
    i = k1
    j = k2
    while i < n and j < n:
        # funkcja zmodyfikowana, by nie wychodzić poza indeks słowa s
        if s[i] == s[j]:
            i += 1
            j += 1
        else:
            if(s[i] < s[j]):
                return "TAK"
            else:
                return "NIE"
    if(j < n):
        return "TAK"
    else:
        return "NIE"


n = int(input("Podaj długość słowa: "))
tab = []
s = ""
for x in range(n):
    l = str(input("Podaj literę słowa: "))
    tab.append(l)
    s += l

ilosc = 0
wynik = [0] * len(tab)

for i in range(len(tab)):
    for j in range(len(tab)):
        if i != j:
            if czy_mniejszy(n,s,i,j) == "TAK":
                ilosc += 1
    wynik[len(tab)-ilosc-1] = i+1
    ilosc = 0

print(wynik)
