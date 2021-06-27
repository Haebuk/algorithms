# 정수 삼각형
n = 5
data = [[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]
def solution(n, list):

    for i in range(1, n):
        for j in range(i+1):
            # 왼쪽 위에서 오는 경우
            if j == 0:
                left_up = 0
            else:
                left_up = list[i-1][j-1]
            # 오른쪽 위에서 오는 경우
            if j == i:
                right_up = 0
            else:
                right_up = list[i-1][j]
            data[i][j] = data[i][j] + max(left_up, right_up)

    
    return max(data[n-1]) 
    
print(solution(n, data))