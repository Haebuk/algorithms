# 카드 정렬하기.py
import heapq
N = int(input())

heap = []
for i in range(N):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_values = one + two
    result += sum_values
    heapq.heappush(heap, sum_values)

print(result)
