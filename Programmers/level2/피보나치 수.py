def solution(n):

    data = [0] * (n+1)
    data[0], data[1] = 0, 1
    for i in range(2, len(data)):
        data[i] = data[i-1] + data[i-2]
    return data[i]%1234567
