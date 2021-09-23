class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

# Runtime: 208 ms, faster than 46.84% of Python3 online submissions for Reverse String.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

# Runtime: 196 ms, faster than 82.28% of Python3 online submissions for Reverse String.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

# Runtime: 184 ms, faster than 98.99% of Python3 online submissions for Reverse String.

