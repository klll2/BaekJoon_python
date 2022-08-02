n,m,k = map(int,input().split(' '))
m1 = m
x = 1.00
y = 1.00
z = 0
while k > 0:
    for i in range(1,k+1):
        y *= m1
        m1 -= 1
        y *= 1/i
        m1 = m
    print(y)
    z += y
    k -= 1
z *= m
for j in range(1,m+1):
    x *= n
    n -= 1
    x *= 1/j
print(z/x)