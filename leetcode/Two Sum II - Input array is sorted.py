class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l + 1, r + 1]
            elif sum > target:
                r -= 1
            else:
                l += 1
            
# Runtime: 56 ms, faster than 96.49% of Python3 online submissions for Two Sum II - Input array is sorted.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(numbers):
            if target - num in dict:
                return [dict[target - num] + 1, i + 1]
            dict[num] = i
            
# Runtime: 56 ms, faster than 96.49% of Python3 online submissions for Two Sum II - Input array is sorted.

