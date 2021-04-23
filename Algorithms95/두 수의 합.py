# 두 수의 합
# 풀이 1. 브루트 포스
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# 풀이 2. in을 이용한 탐색
def twoSum(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

# 풀이 3. 첫 번째 수를 뺀 결과 키 조회
def twoSum(nums, target):
  nums_map = {}
  # 키와 값을 바꿔서 딕셔너리로 저장
  for i, num in enumerate(nums):
    nums_map[num] = i
  print(nums_map)
  # 타겟에서 첫 번째 수를 뺀 결과로 키 조회
  for i, num in enumerate(nums):
    if target - num in nums_map and i != nums_map[target - num]:
      return nums.index(num), nums_map[target - num]

# 풀이 4. 조회 구조 개선
def twoSum(nums, target):
  nums_map = {}
  # 하나의 for 문으로 통합
  for i, num in enumerate(nums):
    if target - num in nums_map:
      return [nums_map[target - num], i]
    nums_map[num] = i

# 풀이 5. 투 포인터 이용
# 정렬된 상태에서만 가능
def twoSum(nums, target):
  left, right = 0, len(nums) - 1
  while not left == right:
    # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
    if nums[left] + nums[right] < target:
      left += 1
    # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
    elif nums[left] + nums[right] > target:
      right -= 1
    else:
      return left, right
  
import time
start = time.time()
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
print("time :", time.time() - start)
