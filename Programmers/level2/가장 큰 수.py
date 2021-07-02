def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)

    return str(int(''.join(numbers))) # 모든 케이스가 0일경우 0으로 만들고 문자열 변경