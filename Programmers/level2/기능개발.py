from collections import deque
def solution(progresses, speeds):
    temp = False
    answer = []
    count = 0
    p = progresses[::-1]
    v = speeds[::-1]

    while p:

        if p[-1] >= 100:
            p.pop()
            v.pop()
            count += 1
            temp = True
            if not p:
                answer.append(count)
                return answer
            else:
                continue
        if not temp & (p[-1] < 100):
            p = [x+y for x,y in zip(p, v)]
            continue
        if temp & ((p[-1] < 100)):
            answer.append(count)
            count = 0
            temp = False

    return answer