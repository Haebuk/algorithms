# 효율적인 화폐 구성

# N: 화폐 종류, M: 만들어야 하는 금액
N, M = map(int, input().split()) 
# 화폐 가치를 저장하는 리스트
data = [int(input()) for _ in range(N)]
# 메모이제이션 리스트 초기화
d = [10001] * 100
d[0] = 0
for i in range(N):
    for j in range(data[i], M+1):
        # (j-i번째 화폐)의 금액을 만들 수 있으면
        # j번째 금액을 (j-i)+1과 이미 저장된 j번째 횟수 중 최소값으로 할당 
        if d[j - data[i]] != 10001:
            d[j] = min(d[j - data[i]] + 1, d[j])
    
if d[M] == 10001: # 만들 수 없으면 -1 출력
    print(-1)
else:
    print(d[M])