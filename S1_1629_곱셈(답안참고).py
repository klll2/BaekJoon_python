A,B,C=map(int,input().split())
def power(a,b,c):

    if b==1:
        return a%c
    elif b==2:
        return (a*a)%c
    
    else:
        if b%2:
            return ((power(a,b//2,c)**2)*a)%c

        else:
            return ((power(a,b//2,c)**2))%c

print(power(A,B,C))

#############################################################3

a,b,c = map(int,input().split(' '))
l = [a]*b
map(str,l)
map(int,l)
k = 1
def recur(l,c,k):
    while l[0] < c and len(l) > 1:
        if len(l) % 2 == 1 and len(l) != 1:
            l.append(1)
        k = l[-1]*l[-2]
        a = l[0]*l[1]
        b = int(len(l)/2)
        l = [a]*b
        map(str,l)
        map(int,l) 
        if k != l[0]:
            l.append(k)
            del l[-2]
    for i in range(0,len(l)):
        l[i] = l[i] % c
    if len(l) == 1:
        print(l[0]%c)
    else:
        recur(l,c,k)

recur(l,c,k)

###################################################################

a,b,c = map(int,input().split(' '))
k = 1
while b > 1:
    if a > c:
        a = a % c
    if b % 2 == 1:
        k *= a
        k = k % c
        a *= a
        b = int(b/2)+1
        a = a % c  
    else:
        a *= a*k
        b = b / 2
        a = a % c
print(a)