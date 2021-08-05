from collections import deque
graph = [
    [],
    [2,3],
    [3,4],
    [],
    []
]
distance = [-1] * 5
count = 1
q = deque()
q.append(1)
distance[1] = 0
while q:
    x = q.popleft()
    for i in graph[x]:
        if distance[i] == -1:
            distance[i] = distance[x] + 1
        q.append(i)
distance.sort()
for i, d in enumerate(distance):
    if d == 2:
        print(i)
if 2 not in distance:
    print(-1)
    