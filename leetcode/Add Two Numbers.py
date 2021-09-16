# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0; # 덧셈이 10 넘을 경우에 1을 담아줌
        res = n = ListNode(0) # res와 n을 같은 주소로 할당해줌. 처음 val=0, next=None
        while l1 or l2 or carry: #l1, l2, carry가 존재할 경우
            if l1:
                carry += l1.val # carry에 l1.val을 더해줌
                l1 = l1.next # l1은 다음 ListNode로 이동
            if l2: # l2도 l1과 동일
                carry += l2.val #
                l2 = l2.next
            carry, val = divmod(carry, 10) # carry를 10으로 나눈 몫과 나머지를 할당
            n.next = n = ListNode(val) # n.next는 ListNode{val:val, next:None}이 되고,
                                        # n도 같은 주소를 가르키고 있음.
                                        # 기존에 n은 res와 주소를 공유하고 있기 때문에
                                        # res = ListNode{val:0, next:ListNode{val:val, next:None}}이 됨

        return res.next # 처음 res.val=0이기 때문에 next만 잡으면 됨

