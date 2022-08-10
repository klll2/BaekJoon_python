t = int(input())
for _ in range(t):
    a,b = map(int,input().split(' '))
    a1 = 1
    b1 = 1
    while a > 0:
        b1 *= b
        a1 *= a
        a -= 1
        b -= 1
    x = b1//a1
    print(x)