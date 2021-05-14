# 음료수 얼려 먹기
n, m = map(int, input().split())
ice = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    # 주어진 범위를 벗어난 경우에 즉시 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if ice[x][y] == 0:
        # 해당 노드 방문 처리
        ice[x][y] = 1
        # 상하좌우 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1
        
print(result)
