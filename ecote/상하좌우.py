# 상하좌우
# 내 풀이

N = input()
axis = list(input().split())

x, y = 1, 1 # 처음 위치

for i in axis:
  if i == 'L' and x != 1:
    x -= 1
  elif i == 'R' and x != int(N):
    x += 1
  elif i == 'U' and y != 1:
    y -= 1
  elif i == 'D' and y != int(N):
    y += 1

print(y, x) # 문제의 좌표가 Y, X순

# 책 풀이

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
  # 이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  # 공간을 벗어나는 경우 무시
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x, y = nx, ny

print(x, y)
