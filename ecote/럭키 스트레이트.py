# 럭키 스트레이트
# 점수 입력
N = input()

# 왼쪽 부분, 오른쪽 부분 자릿수 합
left = 0
right = 0
# 왼쪽 합
for i in range(len(N)//2):
  left += int(N[i])
# 오른쪽 합
for j in range(len(N)//2, len(N)):
  right += int(N[j])
# 대소 비교
if left == right:
  print('LUCKY')
else:
  print('READY')
