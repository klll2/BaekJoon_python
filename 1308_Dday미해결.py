a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
y = b[0] - a[0]
m = b[1] - b[1]
d = b[2] - b[2]
m1 = [1,3,5,7,8,10,12]
m2 = [4,6,9,11]
s = y // 4
y * 365 + s
if a[1] in m1 and b[1] in m1:
        dday = (31 - a[2]) + (31 - b[2])
        for i in range(min(a[1],b[1]),max(a[1],b[1])):
            if i in m1:
                dday += i * 31
            elif i == 2:
                dday += i * 28
            else:
                dday += i * 30