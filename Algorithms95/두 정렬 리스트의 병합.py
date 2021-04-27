# 두 정렬 리스트의 병합
# 풀이 1. 재귀 구조로 연결
def mergeTwoList(l1, l2):
  # l1과 l2중 작은 값이 왼쪽에 오게 만들기
  if (not l1) or (l2 and l1.val > l2.val):
    l1, l2 = l2, l1
  if l1:
    l1.next = mergeTwoList(l1.next, l2)
  return l1
