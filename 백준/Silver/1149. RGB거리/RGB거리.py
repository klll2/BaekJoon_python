"""
- 비고 : 답안 참고 후 제출 (출처 : https://hongcoding.tistory.com/123)

답안을 봤을 때 더 붙잡았어도 이런 풀이는 생각하지 못했을거라 느낌.

* 답안 로직 :
# i-1번째 집과 i+1번째 집은 관계가 없음.
1. 비용과 RGB를 2중 배열로 구현(열 : 집 순서, 행 : RGB)
2. i번째 집의 RGB 선택지에 i-1, i번째 집의 RGB 선택지 중 최소값을 저장
   -> i-1은 i에서 고려되었으므로, i+1에서는 i-1이 아닌 i만 신경쓰면 됨. 
   --> 재귀와 유사한 개념.
       (3*2^n -> 3*2로 계속 유지시킴)
       (선택지가 3*2가 되는 순간 최소값 결정에 의해 양자택일되어 3*2/2 = 3이 되기 때문.)
3. 결국 마지막에 남는 선택지는 3, 셋 중 최소값을 출력.
## 자칫 기하급수적으로 증가할 수 있는 경우의 수를 억제하는 로직을 고안해야 함.
### 경우의 수가 증가하는 원인을 파악, 해당 원인을 해결하도록 로직 고안. 

이해도 : 100%
"""

n = int(input())

cost = []
minCost = -int(1e9)
dp = [[0]*3 for _ in range(n)]
for i in range(n):
    cost.append(list(map(int, input().split())))

dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1] + cost[i][0], dp[i-1][2] + cost[i][0])
    dp[i][1] = min(dp[i-1][0] + cost[i][1], dp[i-1][2] + cost[i][1])
    dp[i][2] = min(dp[i-1][0] + cost[i][2], dp[i-1][1] + cost[i][2])

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))