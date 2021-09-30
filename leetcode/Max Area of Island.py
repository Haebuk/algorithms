class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                grid[x][y] = 0
                return 1 + dfs(x - 1, y) + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
            return 0
        
        maximum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maximum = max(dfs(i, j), maximum)
        return maximum
            
            
# Runtime: 132 ms, faster than 88.04% of Python3 online submissions for Max Area of Island.
