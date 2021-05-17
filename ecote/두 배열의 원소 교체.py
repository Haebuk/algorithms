# 두 배열의 원소 교체
N, K = map(int, input().split()) # N과 K를 입력받기
A = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
B = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

A = sorted(A) # 배열 A는 오름차순 정렬 수행
B = sorted(B, reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며 두 배열의 원소를 최대 K번 비교
for i in range(K):
    # A의 원소가 B의 원소보다 작은 경우
    if A[i] < B[i]:
        # 두 원소를 교체
        A[i], B[i] = B[i], A[i]
    else: # A의 원소가 B의 원소보다 크거나 같은 경우, 반복문 탈출
        break
 
print(sum(A)) # 배열 A의 모든 원소의 합을 출력
