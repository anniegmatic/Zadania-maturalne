a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))

ka = a % 10
kb = b % 10

sumaa = 0
sumab = 0

while a > 0:
    if a < 10:
        pa = a
    sumaa += a % 10
    a = a // 10
    
while b > 0:
    if b < 10:
        pb = b
    sumab += b % 10
    b = b // 10

if sumaa == sumab and(pa == kb or pb == ka):
    print("PRAWDA")
else:
    print("FAŁSZ")
