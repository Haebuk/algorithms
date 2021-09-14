from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        iter = len(text) // len('balloon') # 반복 횟수
        
        text_counts = Counter(text) # text 카운트 계산
        
        for i in range(iter, 0, -1):
            balloon = 'balloon' * i # 반복 횟수 만큼 글자 추가
            balloon_counts = Counter(balloon) # balloon 카운트 계산
            joint_counts = text_counts & balloon_counts # 공통 카운트 계산
            
            # print(f'---{i}---')
            # print('balloon', balloon_counts)
            # print('text', text_counts)
            # print('joint', joint_counts)
            
            # result = text_counts - balloon_counts
            if joint_counts == balloon_counts: # 공통 카운트가 balloon 카운트와 같으면
                return i # 반복 횟수 반환
            
        return 0

"""
다른 사람 풀이
a, b, l//2, o//2, n의 개수를 세서 최소값 반환
cnt = Counter(text)
return min(cnt['a'], cnt['b'], cnt['l']//2, cnt['o']//2, cnt['n'])
"""