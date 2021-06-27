n = int(input())
# 식량 창고 정보
data = list(map(int, input().split()))
# 계산 결과 저장
d = [0] * 100

d[0] = data[0]
d[1] = max(data[0], data[1])
# i번째 식량창고를 털려면 i-2번째 창고를 털었어야 함
# i-1번째 창고를 털면 i번째 창고를 털 수 없음
# 두 케이스 중 더 큰 값을 i번째 값으로 저장
for i in range(2, n):
    d[i] = max(data[i-1], data[i-2] + data[i])

# 마지막 저장 값 출력
print(d[n-1])