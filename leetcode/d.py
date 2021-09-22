class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for _ in range(len(nums)):
            if nums[i] == 0:
                nums.append(nums.pop(i))
                continue
            i += 1
                
            
# Runtime: 48 ms, faster than 82.11% of Python3 online submissions for Move Zeroes.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                
            if nums[left] != 0:
                left += 1
            

#Runtime: 48 ms, faster than 82.11% of Python3 online submissions for Move Zeroes.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            
                
            
        
                
            
        