t = int(input())
l = list(map(int,input().split(' ')))
l1 = []
a = max(l)
b = 0
for i in l:
    c = i/a*100
    b += c
print(b/t)