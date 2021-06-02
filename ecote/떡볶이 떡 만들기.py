# 떡볶이 떡 만들기
N, M = map(int, input().split()) # 떡 개수, 요청 높이
data = list(map(int, input().split())) # 떡 리스트
data.sort() # 떡 길이 정렬 

start = 0 # 제일 짧은 떡
end = max(data) # 제일 긴 떡

while start <= end:
    result = 0 
    H = (start + end) // 2 # 자르는 높이
    for x in data:
        if x > H: # 떡이 높이보다 길 경우
            result += x - H
    if result > M: # 자른 떡이 많을 경우 
        start = H + 1
    elif result < M: # 자른 떡이 적을 경우
        end = H - 1
    else:
        result = H
        break

print(H)


