def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        sum += price * i
    answer = money - sum
    return abs(answer) if answer < 0 else 0