lastNumber = 5
list1 = list(range(1,lastNumber+1,1))
list1.reverse()
j = 0
for i in range(1,lastNumber+1,1):
    for k in range(0,i,1):
        print(list1[j],' ',end='')
        j += 1
    print(end='\n')
    j = 0
