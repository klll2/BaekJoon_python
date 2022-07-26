a,b = map(int,input().split(' '))
q = [i for i in range(1,a+1)]
l = list(map(int,input().split(' ')))
n = 0
x = 0
while len(l) != 0:
    if l[0] == q[0]:
        del q[0]
        del l[0]
    elif q.index(l[0]) > len(q)/2:
        q.insert(0,q[-1])
        del q[-1]
        n += 1
    else:
        q.append(q[0])
        q.remove(q[0])
        n += 1
print(n)
