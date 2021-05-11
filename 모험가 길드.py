# 모험가 길드
n = map(int, input().split())
ranger_list = list(map(int, input().split()))

group = 0 # 총 그룹 수
count = 0 # 현재 그룹의 인원 수
for i in sorted(ranger_list): # 공포도 오름차순 정렬 후 반복
  count += 1 # 현재 그룹 인원 수 1 증가
  if count >= i: # 현재 그룹 인원 수가 공포도보다 크거나 같으면 그룹 수 1 증가
    group += 1
    count = 0 # 초기화

print(group)
