n = int(input("Wczytaj dodatkową liczbę całkowitą: "))

def binarnie(n):
    binarnie = []
    while n > 0:
        if n % 2 == 1:
            binarnie += "1"
        else:
            binarnie += "0"
        n = n // 2
    return binarnie[::-1]

def bloki(znaki):
    b = 1
    for i in range(len(znaki)-1):
        if znaki[i] != znaki[i+1]:
            b += 1
    return b

print(bloki(binarnie(n)))
