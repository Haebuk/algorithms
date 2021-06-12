from bisect import bisect_left, bisect_right

# 일치하는 가사의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어를 길이마다 나눠 저장
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누고, 뒤집어 저장
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 그대로 or 뒤집어서 배열에 삽입
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
        
    for i in range(10001): # 이진 탐색을 위한 정렬
        array[i].sort()
        reversed_array[i].sort()
        
    for q in queries: # 쿼리를 하나씩 처리
        if q[0] != '?': # 처음에 '?'가 오지 않는 경우, 즉 '?'가 마지막에 붙는 경우
            # 좌측 탐색시 '?'를 a로 변경, 우측 탐색시 '?'를 z로 모두 변경
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 처음에 '?'가 붙는 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        
        # 해당하는 단어의 개수 추가
        answer.append(res)
    
    return answer
