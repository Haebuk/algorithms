from collections import deque
def dfs(x, y, count):
    if x >= n or x < 0 or y >= m or y < 0 or graph[x][y] == 0:
        return
    if x == n-1 and y == m-1:
        result.append(count)
    if graph[x][y] == 1:
        graph[x][y] = count
        dfs(x-1, y, count+1)
        dfs(x, y-1, count+1)
        dfs(x+1, y, count+1)

        dfs(x, y+1, count+1)

def bfs(x, y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0 or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n-1][m-1]
result = []
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]
n = len(graph)
m = len(graph[0])
# dfs
dfs(0,0,1)
print('dfs:',min(result))
# bfs
graph = [
    [1,0,1,0,1,0],
    [1,1,1,1,1,1],
    [0,0,0,0,0,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]
print('bfs:',bfs(0,0))