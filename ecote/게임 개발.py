# 게임 개발
A, B = map(int, input().split())
x, y, d = map(int, input().split())
game_map = []
visited = [[0] * B for _ in range(A)]
for _ in range(A):
  game_map.append(list(map(int, input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
# 처음 좌표 방문 처리
visited[x][y] = 1
while True:
  # 왼쪽으로 회전
  turn_left()
  nx = x + dx[d]
  ny = y + dy[d]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
  if visited[nx][ny] == 0 and game_map[nx][ny] == 0:
    visited[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
  else:
    turn_time += 1
  # 네 방향 모두 갈 수 없는 경우
  if turn_time == 4:
    nx = x - dx[d]
    ny = y - dy[d]
    # 뒤로 갈 수 있다면 이동하기
    if game_map[nx][ny] == 0:
      x = nx
      y = ny
    # 뒤가 바다인 경우
    else:
      break
    turn_time = 0

# 정답 출력
print(count)

