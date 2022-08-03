n = int(input())
s, e = 0, int((2**63)**0.5)+1  #해당문제 범위
res = 0
while s <= e:
    m = (s+e)//2
    if m**2 >= n:
        res = m
        e = m-1
    else:
        s = m+1
print(res)

이분탐색
############################################
그냥 풀기

n = int(input())
if n**(1/2) - int(n**(1/2)) == 0:
    print(int(n**(1/2)))
else:
    print(int(n**(1/2))+1)