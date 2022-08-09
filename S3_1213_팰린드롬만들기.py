n = list(input())
n.sort()
l = {}
for i in n:
    l[i] = n.count(i)
v = list(l.values())
k = list(l.keys())
v1 = []
s = str()
count = 0
for i in v:
    if i % 2 == 1:
        count += 1
        v1.append(v.index(i))
if count >= 2:
    print("I'm Sorry Hansoo")
else:
    for i in range(0,len(k)):
        s += k[i]*(v[i]//2)
    s1 = list(s)
    s1.reverse()
    s2 = ''.join(s1)
    if count == 1:
        print(s+k[v1[0]]+s2)
    elif count == 0:
        print(s+s2)