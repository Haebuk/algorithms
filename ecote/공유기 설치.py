# 공유기 설치.py

N, C = map(int, input().split())
data = []
for i in range(N):
    data.append(int(input()))
data.sort()

start = 1 # 최소 gap
end = data[-1] - data[0] # 최대 gap
result = 0

while start <= end:
    mid = (start + end) // 2 # 중간 gap
    count = 1 # 설치한 공유기 개수
    value = data[0]
    for i in range(1, N): # 공유기 설치
        if value + mid <= data[i]: 
            value = data[i]
            count += 1
    if count >= C: # C개 이상 공유기 설치 가능할 시, 거리 증가
        start = mid + 1
        result = mid
    else: # C개 이상 공유기 설치 불가 시, 거리 감소
        end = mid - 1

print(result)
