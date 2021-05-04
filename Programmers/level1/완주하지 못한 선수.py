from collections import Counter, defaultdict
def solution(participant, completion):
    part_count = Counter(participant)
    for runner in completion:
        part_count[runner] -= 1  
    answer = list(part_count.elements())[0]
    return answer
