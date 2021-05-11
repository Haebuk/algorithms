# 숫자 카드 게임
n, m = map(int, input().split())

result = 0
min_num = []
for i in range(n):
  data = list(map(int, input().split()))
  min_num.append(min(data))

result = max(min_num)
print(result)
