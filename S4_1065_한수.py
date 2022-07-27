n = int(input())
l = [i for i in range(1,n+1)]
x = 0
for i in l:
    if i < 100:
        x += 1
    elif i//100 - (i//10 - i//100*10) == (i//10 - i//100*10) - (i - i//10*10):
        x += 1
print(x)