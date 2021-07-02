def solution(arr):
    answer = [0,0]
    N = len(arr)
    
    def dfs(x, y, n):
        init = arr[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if arr[i][j] != init:
                    nn = n//2
                    dfs(x, y, nn)
                    dfs(x+nn, y, nn)
                    dfs(x, y+nn, nn)
                    dfs(x+nn, y+nn, nn)
                    return
        answer[init] += 1
         
    dfs(0,0,N)
    return answer