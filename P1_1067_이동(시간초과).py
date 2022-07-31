n = int(input())
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))    
sumlist = []
for _ in range(n):
    x = 0
    for i in range(0,n):
        x += a[i]*b[i]
    sumlist.append(x)
    b.insert(0,b[-1])
    del b[-1]   
print(max(sumlist))