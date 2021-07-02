def solution(n):
    num = 1
    answer = []
    data = [[0]*i for i in range(1,n+1)]
    x, y = -1, 0 # 인덱스
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            data[x][y] += num
            num += 1

    for row in data:
        for i in row:
            answer.append(i)
            
                       
    return answer