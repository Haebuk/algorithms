def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5] # 1이 찍는 방식
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] # 2가 찍는 방식
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3이 찍는 방식
    score = [0, 0, 0] # 각 사람의 맞힌 개수 리스트
    
    for i in range(len(answers)): # 맞힐때마다 +1 
        if s1[i%len(s1)] == answers[i]: # 순환할 수 있게 나머지로 인덱싱
            score[0] += 1
        if s2[i%len(s2)] == answers[i]:
            score[1] += 1
        if s3[i%len(s3)] == answers[i]:
            score[2] += 1
    
    for i, s in enumerate(score, start=1):
        if s == max(score): # score의 최대값과 각 사람의 점수가 같으면 정답에 추가
            answer.append(i)
    
    
    return answer
