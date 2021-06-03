# 정렬된 배열에서 특정 수의 개수 구하기.py

N, x = map(int, input().split())
data = list(map(int, input().split()))

def left_search(list, start, target, end):
     # 첫번째로 나오는 인덱스 찾기

    if start > end:
        return
    m = (start + end) // 2
    # 인덱스가 0 또는 왼쪽값이 타겟값보다 작고, m번째 값이 타겟값과 일치하면 반환
    if (m==0 or list[m-1] < target) & (list[m] == target):
        return m
    elif list[m] >= target: # m번째 값이 타겟값보다 크거나 같으면 왼쪽으로
        return left_search(list, start, target, m-1)
    else:
        return left_search(list, m+1, target, end)

def right_search(list, start, target, end):
    # 마지막으로 나오는 인덱스 찾기

    if start > end:
        return
    m = (start + end) // 2
    # 인덱스가 마지막 또는 오른쪽 값이 타겟값보다 크고, m번째 값이 타겟값과 일치하면 반환 
    if (m==N-1 or list[m+1] > target) & (list[m] == target):
        return m
    elif list[m] > target: # m번째 값이 타겟값보다 크면 왼쪽으로
        return right_search(list, start, target, m-1)
    else:
        return right_search(list, m+1, target, end)


left = left_search(data, 0, x, N-1)
right = right_search(data, 0, x, N-1)
result = right - left + 1
print(result)
