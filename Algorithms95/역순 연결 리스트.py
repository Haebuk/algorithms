# 역순 연결 리스트
# 연결 리스트를 뒤집어라

# 풀이 1. 재귀 구조로 뒤집기
def reverselist(head):
  def reverse(node, prev):
    # node가 비어있으면 최종적으로 prev 호출
    if not node:
      return prev
    next, node.next = node.next, prev
    return reverse(next, node)

  return reverse(head)

# 풀이 2. 반복 구조로 뒤집기
def reverseList(head):
  node, prev = head, None

  while node:
    next, node.next = node.next, prev
    prev, node = node, next

  return prev
