from collections import deque

def solution(prices):
    
    answer = []
    start = 0
    
    for _ in range(len(prices)):
        sec = 0
        q = deque(prices[start:])
        a = q.popleft()
        while q:
            sec += 1
            if a <= q[0]:
                q.popleft()        
            else:
                break
            
        start += 1
        answer.append(sec)
    return answer