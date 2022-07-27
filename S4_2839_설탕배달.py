t = int(input())
k = 0
x = 0
n = t//5
if n >= 1:
    x = t % 5
    k = n
    if x == 1 and t >= 6:
        k += 1
    elif x == 0:
        k = n
    elif x == 4 and t >= 9:
        k += 2
    elif x == 3:
        k += 1
    elif x == 2 and t >= 12:
        k += 2
    else:
        k = -1
elif t == 3:
    k = 1
else:
    k = -1
print(k)