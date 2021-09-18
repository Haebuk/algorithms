class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer, last_match = 0, -1
        used = {}
        for i, c in enumerate(s):
            if c in used and last_match < used[c]:
                last_match = used[c]    
            answer = max(answer, i - last_match)
            used[c] = i
            
        return answer
        