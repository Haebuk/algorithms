from collections import defaultdict
def solution(clothes):
    answer = 1
    dict = defaultdict(int)
    for c in clothes:
        dict[c[1]] += 1
    for i, j in dict.items():
        answer *= (j+1)
    
    
    # answer = combinations(dict.values(), len(dict.keys()))
    return answer -1