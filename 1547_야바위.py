n = int(input())
l = [1,2,3]
for _ in range(0,n):
    a,b = input().split(' ')
    c = int(a)-1
    d = int(b)-1
    l.append(l[c])
    l[c] = l[d]
    l[d] = l[3]
    del l[3]
x = 0
for i in l:
    x += 1
    if i == 1:
        print(x)
    