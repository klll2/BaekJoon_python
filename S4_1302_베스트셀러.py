t = int(input())
l = []
for _ in range(t):
    x = input()
    l.append(x)
l.sort()
y = [0,'y']
for i in l:
    z = l.count(i)
    if y[0] < z:
        y[0] = z
        y[1] = i
print(y[1])