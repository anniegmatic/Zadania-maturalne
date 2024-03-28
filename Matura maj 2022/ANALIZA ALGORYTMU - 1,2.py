n = int(input("Podaj ilość elementów ciągu do permutacji: "))

tab = [0] * n
for i in range(n):
    a = int(input("Podaj element ciągu: "))
    tab[i] = a

zmiany = 0
for i in range(1, n+1):
    if i not in tab:
        zmiany += 1

print(tab,zmiany)
