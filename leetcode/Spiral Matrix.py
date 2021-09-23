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

# 미친 풀이
def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
"""
spiral_order([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

= [1, 2, 3] + spiral_order([[6, 9],
                            [5, 8],
                            [4, 7]])

= [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                     [5, 4]])

= [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                              [5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

= [1, 2, 3, 6, 9, 8, 7, 4, 5]
"""