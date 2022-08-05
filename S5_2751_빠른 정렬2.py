import sys
t = int(sys.stdin.readline())
l = []
for _ in range(t):
    x = int(sys.stdin.readline())
    l.append(x)
l.sort()
for i in l:
    print(i)
    
    ###########################################33
    
    시간초과 방지를 위해 sys.stdin.readline() 을 input() 대신 사용
    프롬프트 안받고 개행문자 안떼서 좀더 빠른데 잘안씀