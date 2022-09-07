import sys
input = sys.stdin.readline

n = int(input())
card = set(map(int, input().split()))   
m = int(input())
card2 = list(map(int, input().split()))

for i in card2:
    if i in card:
        print(1, end=" ")
    else:
        print(0, end=" ")
        
# 시간 단축하려고 input 안쓰고, list대신 set써야됨.
# in list 보다 in set이 더 빠르기 때문