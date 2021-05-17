# 성적이 낮은 순서로 학생 출력하기.py

N = int(input())
# N명의 학생 정보를 입력받아 리스트에 저장
data = []
for _ in range(N):
    a, b = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    data.append((a, int(b)))

# 키를 이용하여 점수를 기준으로 정렬
data = sorted(data, key = lambda x: x[1])
# 정렬된 결과 출력
for i in data:
    print(i[0], end = ' ')

