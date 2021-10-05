class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def perimeter(x, y):
            count = 0
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or not grid[nx][ny]:
                    count += 1
            return count
                    
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    answer += perimeter(i, j)
        return answer
        
# Runtime: 759 ms, faster than 23.98% of Python3 online submissions for Island Perimeter.