n = int(input("Podaj długość ciągu: "))
A = [0] * n
for i in range(n):
    A[i] = int(input("Wczytaj element ciągu: "))

def bloki(tab):
    bloki = 1
    for j in range(n-1):
        if A[j] != A[j+1]:
            bloki += 1
    w = bloki * 2
    return w

bloki(A)

