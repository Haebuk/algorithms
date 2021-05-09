# 섬의 개수
# 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을때, 섬의 개수를 계산하라.
# (연결되어 있는 1의 덩어리 개수를 구하라.)

def numIslands(grid):
  def dfs(i, j):
    # 더 이상 땅이 아닌 경우 종료
    if i < 0 or i >= len(grid) or j < 0 or len(grid[0]) or grid[i][j] != '1':
      return 
    # 방문 한 곳 0 으로 처리
    grid[i][j] = 0
    # 동서남북 탐색
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)

  count = 0
  for i in range(len(grid)): # 행
    for j in range(len(grid[0])): # 열
      # 육지 발견 시 탐색 시작
      if grid[i][j] == 1:
        dfs(i, j)
        # 모든 육지 탐색 후 카운트 1 증가
        count += 1

  return count

