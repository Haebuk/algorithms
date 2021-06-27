# 금광
# 타이핑 하기 귀찮아서 함수형으로 만듦
case1_axis = [3, 4]
case1 = [[1,3,3,2],[2,1,4,1],[0,6,4,7]]
case2_axis = [4, 4]
case2 = [[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]

def solution(axis, case):
    answer = 0
    n, m = axis[0], axis[1]

    for i in range(1, m):
        for j in range(n):
            # 왼쪽 위에서 오는 경우
            if j == 0:
                left_up = 0
            else:
                left_up = case[j-1][i-1]
            # 왼쪽에서 오는 경우
            left = case[j][i-1]
            # 왼쪽 아래에서 오는 경우
            if j == n-1:
                left_bottom = 0
            else:
                left_bottom = case[j+1][i-1]
            case[j][i] = case[j][i] + max(left_up, left, left_bottom)

    for row in case:
        answer = max(answer, max(row)) 
    return answer

print(solution(case1_axis, case1))
print(solution(case2_axis, case2))