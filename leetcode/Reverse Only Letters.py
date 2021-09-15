class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        list_ = list(s) # 뒤에서 부터 pop할 리스트
        answer = list(s) # 정답을 저장할 리스트
        for i in range(len(s)):
            if s[i].isalpha(): # s의 i번째 글짜가 알파벳일 경우
                while list_:
                    a = list_.pop() # 맨 뒷글자 뽑기
                    if a.isalpha(): # a가 알파벳일 경우 i번째 글자를 a로 변경
                        answer[i] = a
                        break
        return ''.join(answer)
                        
# [Python] 2 lines with stack, explained

class Solution:
    def reverseOnlyLetters(self, s):
        stack = [c for c in s if c.isalpha()] # 알파벳인 글자만 담기
        # s 반복문 돌면서 c가 알파벳이면 스택에서 pop 담기. 알파벳 아니면 c
        return "".join(stack.pop() if c.isalpha() else c for c in s)