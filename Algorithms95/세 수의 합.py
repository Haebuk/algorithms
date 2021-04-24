# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트 출력
# 풀이 1. 브루트 포스로 계산
def sumThree(nums):
  results = []
  nums.sort()

  # 브루트 포스 n^3 반복
  for i in range(len(nums) - 2):
    # 중복된 값 건너뛰기
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    for j in range(i + 1, len(nums) - 1):
      if j > i + 1 and nums[j] == nums[j - 1]:
        continue
      for k in range(j + 1, len(nums)):
        if k > j + 1 and nums[k] == nums[k - 1]:
          continue
        if nums[i] + nums[j] + nums[k] == 0:
          results.append((nums[i], nums[j], nums[k]))

  return results

# 풀이 2. 투 포인터로 합 계산
def sumThree(nums):
  results = []
  nums.sort()

  for i in range(len(nums - 2)):
    # 중복된 값 건너뛰기
    if i > 0 and nums[i] == nums[i - 1]:
      continue
      
    # 간격을 좁혀가며 sum 계산
    left, right = i + 1, len(nums) - 1
    while left < right:
      sum = nums[i] + nums[left] + nums[right]
      if sum < 0:
        left += 1
      elif sum > 0:
        right -= 1
      else:
        # sum = 0인 경우이므로 정답
        results.append((nums[i], nums[left], nums[right]))
        # 양 옆 동일한 값 스킵
        while left < right and nums[left] == nums[left + 1]:
          left += 1
        while left < right and nums[right] == nums[right - 1]:
          right -= 1
        # sum = 0인 상황이므로 한 쪽만 이동하면 어차피 sum=0 될 수 없으므로 둘 다 이동
        left += 1
        right -= 1


nums = [-1, 0, 1, 2, -1, 4]
print(sumThree(nums))

