from itertools import permutations
import math
def solution(numbers):
    answer = 0
    
    m = []
    n = [] 
    for i in range(1,len(numbers)+1):
        m.append(list(permutations(numbers, i)))

    for i in m:
        for j in i:
            n.append(''.join(j))
    
    n = list(set(map(int, n)))
    print(n)
    
    max_n = max(n)
    data = [True] * (max_n+1)
    for i in range(2, int(math.sqrt(max(n)) + 1)): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if data[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= max_n:
                data[i * j] = False
                j += 1

    sosu = [i for i in range(2, max_n+1) if data[i]]

    for i in n:
        if i in sosu:
            answer += 1
    return answer