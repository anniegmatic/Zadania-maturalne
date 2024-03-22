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
for x in range(n):
    tab.append(str(input("Podaj literę słowa: ")))

print(czy_mniejszy(n,s,k1,k2))

'''
slowa1: TAK
slowa2: NIE 
slowa3: NIE
'''
