n = int(input())
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))    
x = 0
while len(a)>0:
    x += min(a)*max(b)
    a.remove(min(a))
    b.remove(max(b))
print(x)