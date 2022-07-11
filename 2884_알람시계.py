a,b = input().split(' ')
c = int(a)-1
d = int(b)-45
if c <= 0:
    c = 24+c
    if c == 24:
        c = 0
if d < 0:
    d = 60+d
    a = c
print(a,d)