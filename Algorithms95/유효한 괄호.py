# 유효한 괄호
# 괄호로 된 입력값이 올바른지 판별하라

# 풀이 1. 스택 일치 여부 확인
def isValid(s):
  stack = []
  table = {
    ')': '(',
    '}': '{',
    ']': '[',
  }

  # 스택 이용 예외 처리 및 일치 여부 판별
  for char in s:
    # 테이블에 존재하지 않으면 푸시
    if char not in table:
      stack.append(char)
    # 스택이 비어있거나 팝했을 때 결과가 일치하지 않으면 False 리턴
    elif not stack or table[char] != stack.pop():
      return False
  return len(stack) == 0
