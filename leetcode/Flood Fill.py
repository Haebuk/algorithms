class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n, original_color = len(image), len(image[0]), image[sr][sc]
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            if image[x][y] == newColor or image[x][y] != original_color:
                return
            image[x][y] = newColor
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        dfs(sr, sc)
        return image
    
# Runtime: 80 ms, faster than 44.24% of Python3 online submissions for Flood Fill.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n, original_color = len(image), len(image[0]), image[sr][sc]
        if original_color != newColor:
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == original_color:
                        q.append((x, y))
        return image
            
#Runtime: 76 ms, faster than 71.13% of Python3 online submissions for Flood Fill.
    
            
            
        