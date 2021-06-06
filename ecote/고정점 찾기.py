# 고정점 찾기.py

N = int(input())
data = list(map(int, input().split()))

start = 0
end = len(data) - 1
result = 0

while start <= end:
    m = (start + end) // 2
    print(start, end, m)
    if data[m] == m: # 인덱스와 가리키는 값이 일치하면 인덱스 반환
        result = m  
        break
    elif data[m] < m: # 인덱스가 큰 경우
        start = m + 1
    else: # 인덱스가 작은 경우
        end = m - 1
    result = -1 # result -1로 할당, 어차피 data[m] == m 이면 break 니까

print(result)
