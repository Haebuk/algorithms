# 만들 수 없는 금액

# 동전 개수 입력
n = map(int, input().split())
# 각 동전 입력받아 리스트로 변환
coin = list(map(int, input().split()))

target = 1
# 동전 크기 오름차순 정렬 후 반복
for i in sorted(coin):
  if target < i: # i번째 동전보다 target 값 작으면 종료.
    break
  target += i # target + i번째 동전 값

print(target) # target 출력

# target 값보다 작은 동전이 존재시 이 동전들을 통해 target값 조합가능. target값 보다 큰 동전이 오면 불가능
