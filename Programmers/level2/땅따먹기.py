def solution(land):

    width = len(land[0])
    height = len(land)
    
    for i in range(1,height):
        for j in range(width):
            # print(max(land[i-1][:j] + land[i-1][j:]))
            land[i][j] = max(land[i-1][:j] + land[i-1][j+1:]) + land[i][j]

    return max(land[-1])