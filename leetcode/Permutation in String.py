class Solution:
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        
        target = [0] * 26
        for x in A:
            target[x] += 1
            
        window = [0] * 26
        for i, n in enumerate(B):
            window[n] +=1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if target == window:
                return True
        return False
        

# Runtime: 64 ms, faster than 88.58% of Python3 online submissions for Permutation in String.
