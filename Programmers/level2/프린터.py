from collections import deque 
import heapq
def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    m = max(q)
    
    while q:
        a = q.popleft() # 큐에서 첫 번째 값 추출
        
        if (location == 0) & (a == m):# 내가 찾는 값일 때 반환, 종료
            return answer
        
        location -= 1
        if location == -1:
            location = len(q)
            
        if a >= m: # a가 최대값일 때 그냥 빠짐 
            answer += 1 # 출력 횟수 증가
            m = max(q)  # 최대값이 빠졌으므로 최대값 초기화
            
        else: # a가 최대값이 아닐 때
            q.append(a) # 다시 큐의 마지막에 삽입
        print(a, location, answer)
        
            
        
            

    return answer