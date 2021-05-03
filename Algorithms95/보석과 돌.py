# 보석과 돌
# J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.

# 풀이 1. 해시 테이블을 이용한 풀이
def numJewelsInStones(J, S):
  freqs = {}
  count = 0

  # 돌(S)의 빈도 수 계산
  for char in S:
    if char not in freqs:
      freqs[char] = 1
    else:
      freqs[char] += 1

  # 보석(J)의 빈도 수 합산
  for char in J:
    if char in freqs:
      count += freqs[char]

  return count

  # 풀이 2. defaultdict를 이용한 비교 생략
  def numJewelsInStones(J, S):
    freqs = collections.defaultdict(int)
    count = 0

    # 비교 없이 돌(S) 빈도 수 계산
    for char in S:
      freq[char] += 1

    # 비교 없이 보석(J) 빈도 수 합산
    for char in J:
      count += freqs[char]

    return count

  # 풀이 3. Counter로 계산 생략
  def numJewelsInStones(J, S):
    freqs = collections.Counter(S) # 돌(S) 빈도 수 계산
    count = 0

    # 비교 없이 보석(J) 빈도 수 합산
    for char in J:
      count += freqs[char]

    return count

  # 풀이 4. 파이썬다운 방식
  def numJewelsInStones(J, S):
    return sum(s in J for s in S)
