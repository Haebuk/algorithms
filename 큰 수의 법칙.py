# 큰 수의 법칙
# N, M, K 순으로 입력 받기
n, m, k = map(int, input().split())
# N 개의 수 공백 구분하여 입력 받기
num_list = list(map(int, input().split()))

# 데이터 크기 순 정렬
num_list.sort()
first = num_list[n-1] # 첫 번째 큰 수 
second = num_list[n-2] # 두 번째 큰 수 

result = 0

while True:
  for i in range(k): # 가장 큰 수 K번 더하기
    if m == 0: # m=0 이면 탈출
      break
    result += first 
    m -= 1 # 더할 때 마다 1씩 빼기
  if m == 0:
    break
  result += second # 두 번째 큰 수 한 번 더하기
  m -= 1
print(result)
