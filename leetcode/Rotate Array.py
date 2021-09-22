class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k, n = k % len(nums), len(nums) - 1
        reverse(0, n)
        reverse(0, k - 1)
        reverse(k, n)
                
        
# Runtime: 228 ms, faster than 62.09% of Python3 online submissions for Rotate Array.

from collections import deque
class Solution:
    def rotate(self, nums: List[int], k:int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = deque(nums)
        for _ in range(k):
            d.appendleft(d.pop())
        nums[:] = list(d)

# Runtime: 212 ms, faster than 86.27% of Python3 online submissions for Rotate Array.

from collections import deque
class Solution:
    def rotate(self, nums: List[int], k:int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = deque(nums)
        d.rotate(k)
        nums[:] = list(d)

# Runtime: 216 ms, faster than 80.57% of Python3 online submissions for Rotate Array.