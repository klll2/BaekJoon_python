t = int(input())
lx = []
ly = []
n = 0
s1 = 0
s2 = 0
l = {}
for _ in range(t):
    x,y = map(int,input().split(' '))
    lx.append(x)
    ly.append(y)
for i in range(0,t):
    s1 = lx[i]
    s2 = ly[i]
    n += (lx.count(lx[i])+ly.count(ly[i]))
    l[n] = [s1,s2]
    n = 0
n = sum(list(l.keys()))
print(l,n)