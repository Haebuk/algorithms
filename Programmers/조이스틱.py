import string
def solution(name):
    answer, count = 0, 0
    data = []
    alist = list(string.ascii_uppercase)
    for a in name:
        data.append(min(alist.index(a), (26-alist.index(a))))
    idx = 0
    
    while True:
        answer += data[idx]
        data[idx] = 0
        if sum(data) == 0:
            return answer
        
        left, right = 1, 1
        while data[idx-left] == 0: 
            left += 1
        while data[idx+right] == 0:
            right += 1
        answer += left if left<right else right
        idx += -left if left<right else right
    
    
    return answer