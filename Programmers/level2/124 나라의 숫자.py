def solution(n):
    if n <= 3:
        return '124'[n-1]
    else:
        
        d, r = divmod(n-1, 3)
        
    return solution(d) + '124'[r]