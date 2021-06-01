# 부품 찾기.py
N = int(input())
store = list(map(int, input().split()))
M = int(input())
user = list(map(int, input().split()))
store.sort()

# 재귀적 이진탐색
def binary_search(array, start, target, end):
    if start > end: # 찾는 원소가 없는 경우 none 반환 
        return None
    mid = (start + end) // 2 # 중앙값 
    if array[mid] == target: # 찾는값과 중앙값 일치 시 mid 반환
        return mid
    elif array[mid] > target: # 찾는값이 왼쪽에 있는 경우
        return binary_search(array, start, target, mid - 1)
    else: # 찾는값이 오른쪽에 있는 경우
        return binary_search(array, mid + 1, target, end)

for item in user:
    result = binary_search(store, 0, item, N)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
