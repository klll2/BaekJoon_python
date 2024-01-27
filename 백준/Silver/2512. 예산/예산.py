import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
m = int(input())

def budget(n,m,l):
    
    c = m//n
    fix_c = m//n
    low_sum = 0
    l = sorted(l)
    i = 0

    while i < n:
        
        if l[-1] <= c:
            return l[-1]
        
        if l[i] <= c:
            low_sum += l[i]
            i += 1
            c = (m - low_sum)//(n - i)
            
        else:
            if l[-1] < fix_c:
                b = l[-1]
                
            else:
                b = (m - low_sum)//(n - i)
                
            return b

print(budget(n,m,l))