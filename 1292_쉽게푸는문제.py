a1,b1 = input().split(' ')
a = int(a1)-1
b = int(b1)
l = []
for i in range(1,1000):
    for _ in range(0,i):
        l.append(i)
c = sum(l[a:b])
print(c)