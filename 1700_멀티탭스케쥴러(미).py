a1,b1 = input().split(' ')
c1 = list(input().split(' '))
a = int(a1)
c = list(set(c1))
print(c)
del c[0:a]
print(c)
b = len(c)
print(b)
GG