def solution(array, commands):
    answer = []
    
    for arr in commands:
        # 커맨드의 숫자를 각각 i, j, k로 받기
        i, j, k = arr[0], arr[1], arr[2]
        # i부터 j까지 배열 자르기
        cut = array[i-1:j]
        # 배열 정렬
        cut.sort()
        # k번째 수 answer 리스트에 추가
        answer.append(cut[k-1])
        
    return answer
