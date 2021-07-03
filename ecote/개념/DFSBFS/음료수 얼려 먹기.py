from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    if data[x][y] == 1:
        return False
    while q:
        x, y = q.popleft()
        data[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if data[nx][ny] == 0:
                q.append((nx, ny))
            
    return True

def dfs(x, y):
    if x >= n or x < 0 or y >= m or y < 0:
        return False
    if data[x][y] == 0:
        data[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


result = 0
data = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
n = len(data)
m = len(data[0])
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if bfs(i, j) == True:
            result += 1
print(result)
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)