def SumaKwCyfr(n):
    suma = 0
    while n >0:
        suma += (n % 10) ** 2
        n = n//10
    return suma

def nudna(suma):
    for i in range(1000):
        if suma != 1:
            suma = SumaKwCyfr(suma)
        else:
            return True
    return False
            
        

n = int(input("Podaj dodatnią liczbę całkowitą: "))
print(nudna(SumaKwCyfr(n)))
