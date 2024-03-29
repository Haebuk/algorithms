class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        ntoa = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        
        answer = []
        def dfs(idx, string):
            # 종료 조건
            if len(string) == len(digits):
                answer.append(string)
                return
            
            for i in range(idx, len(digits)):
                for j in ntoa[digits[i]]:
                    dfs(i + 1, string + j)
                    
        dfs(0, "")
        if not digits:
            return []
                
        return answer