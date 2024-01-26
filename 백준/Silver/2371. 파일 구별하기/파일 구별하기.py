import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    f = list(map(int,input().split()))
    l.append(f[:-1])

def equalen(l):
    maxlen = max(list(map(lambda x: len(x), l)))
    for i in l:
        while len(i) < maxlen:
            i.append(0)
    return l           


def dsgs(l):
    k = [1]
    le = 1
    c = 0
    l2 = list(map(lambda x: x[:le], l))
    while l2.count(l2[c]) > 1 and c < len(l2):
        le += 1
        l2 = list(map(lambda x: x[:le], l))
        if l2.count(l2[c]) == 1:
            k.append(le)
            le = 1
            c += 1
    return max(k)

print(dsgs(equalen(l)))

