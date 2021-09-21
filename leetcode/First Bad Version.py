# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start <= end:
            print(start , end)
            mid = (start + end) // 2
            if not isBadVersion(mid): # mid가 불량 아니면
                start = mid + 1
            elif not isBadVersion(mid-1): # mid가 불량인데 mid-1이 불량이 아니면
                return mid
            else:
                end = mid - 1
        return mid

# Runtime: 32 ms, faster than 62.80% of Python3 online submissions for First Bad Version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start

        
        