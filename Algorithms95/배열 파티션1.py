# 배열 파티션 1
# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수 출력

# 풀이 1. 오름차순 풀이
def arrayPairSum(nums):
  sum = 0
  pair = []
  nums.sort()

  for n in nums:
    # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
    pair.append(n)
    if len(pair) == 2:
      sum += min(pair)
      pair = []

  return sum

nums = [1, 4, 3, 2]
print(arrayPairSum(nums))