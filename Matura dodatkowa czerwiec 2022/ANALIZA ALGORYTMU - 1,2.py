def SumaKwCyfr(n):
    suma = 0
    while n >0:
        suma += (n % 10) ** 2
        n = n//10
    return suma

n = int(input("Podaj dodatnią liczbę całkowitą: "))
print(SumaKwCyfr(n))
