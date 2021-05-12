# 시각
# N 입력 받기
N = int(input())

if N >= 3 and N < 13:
    count = 3600 + N * 1575
elif N >= 13 and N < 23:
    count = 7200 + (N - 1) * 1575
elif N >= 23:
    count = 3600 * 3 + (N - 2) * 1575

print(count)

# 책 풀이
# H를 입력받기
h = int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k):
        count += 1

print(count)
