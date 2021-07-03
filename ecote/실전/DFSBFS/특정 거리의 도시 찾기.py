from collections import deque
def dfs(x, count):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i, count+1)
    result.append(count)
    
count = 0
result = []
graph = [
    [],
    [2,3],
    [3,4],
    [],
    []
]
n = len(graph)
visited = [False] * n
dfs(1,count)
print(result)

