import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n # 오큰수가 아니라면 전부 -1로 반영하기 때문에 굳이 바꾸는 과정 필요 X
stack = []

stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
# while stack / and /  while A[stack[-1]] < A[i]로 나누어 작동
# stack에 요소가 1개 이상, A[stack[-1] -> 마지막으로 넣은 A값의 인덱스] < A[i]이어야 작동
        answer[stack.pop()] = A[i]
# A[i]보다 작은 값을 모두 A[i] = 오큰수 로 바꿈
# answer에는 오큰수 및 -1만 저장, stack에는 아직 값이 배정되지 않은 A의 인덱스들만 저장
    stack.append(i)

print(*answer) # *list -> 각 리스트의 요소들을 띄어쓰기로 연결해 출력
