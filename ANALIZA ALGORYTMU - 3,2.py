def pot(a, x, M):
    if x == 0:
        return 1
    if x % 2 == 0:
        w = pot(a, x//2, M)
        return (w*w) % M
    if x % 2 == 1:
        w = pot(a, (x-1)//2, M)
        return (a*w*w) % M

a = int(input("a: "))
x = int(input("x: "))
M = int(input("M: "))

print(pot(a, x, M))

