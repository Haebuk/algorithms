def solution(A,B):
    answer = 0
    # 최솟값이 나오려면 한쪽에서는 최소, 한쪽에서는 최대값을 더해야 함
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer