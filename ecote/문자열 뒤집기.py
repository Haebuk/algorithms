# 문자열 뒤집기
n = input()
# 카운트 초기화
count0 = 0
count1 = 1
# 입력값 처음부터 끝까지 반복
for i in range(len(n)-1):
  if int(n[i]) != int(n[i+1]): # 현재 수와 다음 수가 다른 경우
    if int(n[i+1]) == 0: # 현재 수가 1, 다음 수가 0 인 경우 
      count1 += 1
    elif int(n[i+1]) == 1: # 현재 수가 0, 다음 수가 1인 경우
      count0 += 1

print(min(count0, count1)) # 최솟값 
