# 중복 문자 없는 가장 긴 부분 문자열
# 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라.

# 풀이 1. 슬라이딩 윈도우와 투 포인터로 사이즈 조절
def lengthOfLongestSubstring(s):
  used = {}
  max_length = 0
  start = 0
  for index, char in enumerate(s):
    # 이미 등장했던 문자라면 start 위치 갱신 (+ 슬라이딩 윈도우 바깥에 있는 문자 무시)
    print(index, char)
    if char in used and start <= used[char]:
      start = used[char] + 1
      print('start:',start)
    else: # 최대 부분 문자열 길이 갱신
      max_length = max(max_length, index - start + 1)
      print('max_length:',max_length)
    
    # 현재 문자의 위치 삽입
    # used[char]는 현재 문자를 키로 하는 해시 테이블, 값은 현재 위치
    used[char] = index
    print('used:',used[char])

  return max_length

s1 = 'abcabcbb'
s2 = 'bbbbb'
s3 = 'pwwkew'

lengthOfLongestSubstring(s1)
lengthOfLongestSubstring(s2)
lengthOfLongestSubstring(s3)
