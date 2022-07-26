a = list(input())
a = list(map(int,a))
n = 0
while len(a) >= 2:
    a = list(str(sum(a)))
    a = list(map(int,a))
    n += 1
print(n)
if sum(a)/3 - sum(a)//3 == 0:
    print("YES")
else:
    print("NO")