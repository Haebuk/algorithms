class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])

# Runtime: 408 ms, faster than 11.76% of Python3 online submissions for Squares of a Sorted Array.

from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        squared = [num**2 for num in nums]
        answer = deque()
        while left <= right:
            if squared[left] < squared[right]:
                answer.appendleft(squared[right])
                right -= 1
            else:
                answer.appendleft(squared[left])
                left += 1
        return list(answer)

        
# Runtime: 363 ms, faster than 17.56% of Python3 online submissions for Squares of a Sorted Array.