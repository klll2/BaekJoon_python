t = int(input())
count = 0
check = 0
vic = 0
for _ in range(0,t):
    x = list(map(int,input().split(' ')))
    x.sort()
    print(x)
    for i in range(0,len(x)):
        if x[i] != x[i-1] and i != 0 and x[i] != x[-1]:
            print(x[i-1],x[i])
            count = len(x[check:i])
            print(count)
            check = i
            if count >= len(x)/2:
                print(count)
                vic += 1
                print(x[i-1])
            else:
                count = 0
        elif x[i] == x[-1]:
            print(x[i],x[-1])
            count = len(x)-i+1
            print(count)
            if count >= len(x)/2:
                vic += 1
                print(x[i-1])
    if vic == 0:
        print('SYJKGW')