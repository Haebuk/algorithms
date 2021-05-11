# 곱하기 또는 더하기
n = input()
# 첫번째 숫자 
result = int(n[0])

for i in range(1, len(n)):
    num = int(n[i]) # i번째 수
    if num <= 1 or result <= 1: # 0,1 인 경우 덧셈
        result += num
    else:
        result *= num # 그 외 곱셈

print(result)
