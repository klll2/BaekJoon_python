a,b,c,d = map(int,input().split(' '))
x = 0
if 2*c > d and d > c:
    x += min(a,b)*d
    x += ((a+b)-2*min(a,b))*c
elif c >= d:
    x += min(a,b)*d
    if (max(a,b)-min(a,b)) % 2 == 1:
        x += ((a+b)-2*min(a,b)-1)*d+c
    else:
        x += ((a+b)-2*min(a,b))*d
else:
    x = (a+b)*c
print(x)     