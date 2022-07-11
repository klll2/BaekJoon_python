n = int(input())
for i in range(0,n):
    a = ' '*(i)+'*'*(2*(n-i)-1)
    print(a)
for i in range(1,n):
    b = ' '*(n-i-1)+'*'*(2*i+1)
    print(b)
