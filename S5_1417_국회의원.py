t = int(input())
l = []
for _ in range(0,t):
    x = int(input())
    l.append(x)
if t == 1:
    print(0)
else:
    d = l[0]
    n = 0
    del l[0]
    while max(l) >= d:
        l.sort()
        l.reverse()
        l[0] -= 1
        d += 1
        n += 1
    print(n)