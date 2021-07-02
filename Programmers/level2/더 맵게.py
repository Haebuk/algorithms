import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 우선순위 큐로 만듦 -> 자동으로 오름차순 정렬됨

    while scoville:
        if scoville[0] < K: # 첫 번째 음식의 스코빌 지수가 K보다 작을 경우
            # 제일 안 매운 두 음식 뽑기
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            # 두 음식 섞기
            c = a + 2 * b
            # 섞은 음식 큐에 추가
            heapq.heappush(scoville, c)
            # 섞은 횟수 증가
            answer += 1
        else: # 첫 번째 음식의 스코빌 지수가 K이상일 경우 종료
            break
        if (len(scoville) == 1) & (scoville[0] < K): # 하나 남은 음식의 스코빌 지수가 K이하일 경우 -1 리턴
            return -1
        
    return answer