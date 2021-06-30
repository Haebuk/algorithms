def solution(s):
    s = s.split(' ')
    data = []
    for word in s:
        answer = ''
        for i in range(len(word)):
            if i==0 and isinstance(word[i], str):
                answer += word[i].upper()
            elif isinstance(word[i], int):
                answer += word[i]
            elif i!=0 and isinstance(word[i], str):
                answer += word[i].lower()
        data.append(answer)
            
            
    return ' '.join(data)