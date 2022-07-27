t = int(input())
l = [[0,1],[1,0]]
for _ in range(t):
    n = int(input())
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    elif n == 2:
        print('1 1')
    elif n == 3:
        print('1 2')
    else:
        i = 1
        while i < n:
            l.insert(0,[l[0][0] + l[1][0], l[0][1] + l[1][1]])
            del l[2]
            i += 1 
        print(l[0][0],l[0][1])
        l = [[0,1],[1,0]]