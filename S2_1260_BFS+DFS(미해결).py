def dfs(graph, start):
    vst = list()
    nvst = list()
    
    nvst.append(start)
    
    while nvst:
        n = nvst.pop()
        if n not in vst:
            vst.append(n)
            nvst.extend(graph[n])
    
    return vst

def bfs(graph, start):
    vst = list()
    nvst = list()
    
    nvst.append(start)

    while nvst:
        n = nvst.pop(0)
        if n not in vst:
            vst.append(n)
            nvst.extend(graph[n])

    return vst
            
if __name__ == "__main__":
    n,m,v = map(int,input().split(' '))
    graph = {}
    for _ in range(m):
        a,b = map(int, input().split(' '))
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

    print(dfs(graph, v))
    print(bfs(graph, v))
        