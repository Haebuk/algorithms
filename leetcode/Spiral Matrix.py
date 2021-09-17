class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        answer = []
        x, y, dx, dy = 0, 0, 1, 0
        for _ in range(m*n):
            if not 0 <= x + dx < n or not 0 <= y + dy < m or matrix[y+dy][x+dx] == -1000:                
                dx, dy = -dy, dx
            answer.append(matrix[y][x])
            matrix[y][x] = -1000
            x, y = x + dx, y + dy
        return answer