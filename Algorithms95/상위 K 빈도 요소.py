# 상위 K 빈도 요소
# k번 이상 등장하는 요소를 추출하라.
import collections

def topKFrequent(nums, k):
  return list(zip(*collections.Counter(nums).most_common(k)))[0]
