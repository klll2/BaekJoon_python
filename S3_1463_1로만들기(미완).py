n = int(input())
x = 0
while n != 1:
    if (n - 1) % 3 == 0:
        n = (n - 1) / 3
        x += 2
    elif (n - 1) % 2 == 0 and n != 3:
        n = (n - 1) / 2
        x += 2
    elif n % 3 == 0:
        n = n / 3
        x += 1
    elif n % 2 == 0:
        n = n / 2
        x += 1
    else:
        n -= 1
        x += 1
print(x)