def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            addition = numbers[i] + numbers[j]
            answer.append(addition)

    answer = set(answer)
    answer = sorted(list(answer))

    return answer
