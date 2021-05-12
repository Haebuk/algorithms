# 볼링공 고르기
# 내 풀이
N , M = map(int, input().split())
ball = list(map(int, input().split()))

count = 0 
for i in range(len(ball)-1):
  for j in range(i+1, len(ball)):
    if ball[i] != ball[j]:
      count += 1

print(count)

# 효율적인 풀이
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11
for x in data:
  # 각 무게에 해당하는 볼링공의 수 카운트
  array[x] += 1
  
 result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
  n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  result += array[i] * n
  
print(result)
