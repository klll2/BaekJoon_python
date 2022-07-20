a, b = map(int, input().split())
li = [1]*(b-a+1)
for i in range(2, int(b**0.5)+1):
    t = i**2
    for j in range(a//t*t, b+1, t): 
        # a//t*t -> 보정(ex.a = 15 t = 16이면 a = 16부터 시작)
        # t -> 배수(상동일 때, j = 16, 20, 24, ....)
        if j >= a and li[j-a]:
            # j >= a -> 범위 충족
            # li[j-a] -> 리스트는 b-a+1개이므로,
            li[j-a] = 0
            # boolean 배열로 중복을 없앰.
print(li.count(1))
