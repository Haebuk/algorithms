def solution(s):
    answer = ''
    ind = len(s) // 2
    if len(s) % 2 == 0: # 단어 길이 짝수
        answer = s[ind-1] + s[ind]
    else: # 단어 길이 홀수
        answer = s[ind]
    return answer
