numbers = set(range(1,10000))
remove_set = set()
for num in numbers:
    for n in str(num):
        num += int(n)
    remove_set.add(num)
    
self_numbers = numbers - remove_set
for self_num in sorted(self_numbers):
    print(self_num)
    
    ################################################
    
    i = 1
x = 0
l = []
lastx = 0
while x <= 10000:
    x = i + (i//1000) + (i//100) + (i//10) + (i%10)
    l.append(x)
    i += 1
for j in range(0,10001):
    if j not in l:
        print(j)