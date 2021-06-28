def solution(prices):
    
    answer = [0] * len(prices)
    
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1 # 가격 한 번은 유지됨
                break
    
    return answer