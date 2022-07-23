a = 0
b = 0
n = 1
for _ in range(9):
    x = int(input())
    if x > a:
        a = x
        b = n
    n += 1
print(a)
print(b)