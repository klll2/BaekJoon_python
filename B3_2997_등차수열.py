a = list(map(int,input().split(' ')))
a.sort()
x = []
for i in range(0,len(a)-1):
    x.append(a[i+1] - a[i])
if x[0] == x[1]:
    print(a[2]+x[0])
else:
    print(a[x.index(max(x[0],x[1]))]+min(x[0],x[1]))