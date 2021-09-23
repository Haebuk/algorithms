class Solution:
    def reverseWords(self, s: str) -> str:
        list_ = s.split(' ')
        for i, string in enumerate(list_):
            l, r = 0, len(string) - 1
            string = list(string)
            while l < r:
                string[l], string[r] = string[r], string[l]
                l += 1
                r -= 1
            list_[i] = ''.join(string)
        return ' '.join(list_)
# Runtime: 68 ms, faster than 31.16% of Python3 online submissions for Reverse Words in a String III.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split(' ')])
    
# Runtime: 32 ms, faster than 87.58% of Python3 online submissions for Reverse Words in a String III.
