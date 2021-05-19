# 국영수.py
N = int(input())
data = []

# 모든 학생들의 정보를 입력받기
for _ in range(N):
    a, b, c, d = input().split()
    data.append((a, int(b), int(c), int(d)))
# 정렬
data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
# 출력
for i in data:
    print(i[0])
