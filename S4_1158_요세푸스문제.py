a,b = map(int,input().split(' '))
l = list(range(1,a+1))
c = b
r = []
for _ in range(a):
    if c > len(l):
        c -= len(l)
        while 0 in l:
            l.remove(0)
        while c > len(l):
            c -= len(l)
        r.append(l[c-1])
        l[c-1] = 0
        c += b
    else:
        r.append(l[c-1])
        l[c-1] = 0
        c += b

print("<" + ", ".join(list(map(str, r))) + ">")
        