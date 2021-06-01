# 실패율.py

N = int(input())
stages = list(map(int, input().split()))
stages.sort()
result = []

length = len(stages)
fail_rate = []
for i in range(1, N+1):
    count = stages.count(i)
    fail = count / length
    fail_rate.append((i, fail))
    length -= count

fail_rate.sort(key = lambda x: x[1], reverse=True)
for i, j in fail_rate:
    result.append(i)

print(result)
    
