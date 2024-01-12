import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m,start = map(int,input().split())

graph = [ [] for _ in range(n) ]
visited = [False]*n

def dfs(start):
    
    if not visited[start-1]:
        print(start)
        visited[start-1] = True
        
        for i in sorted(graph[start-1]):
            dfs(i+1)

            
def bfs(start):
    
    queue = deque()
    queue.append(start-1)
    visited = [False]*n
    
    while queue:
        start = queue.popleft()
        
        if not visited[start]:
            print(start+1)
            visited[start] = True
            queue += sorted(graph[start])

for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

    
dfs(start)
bfs(start)