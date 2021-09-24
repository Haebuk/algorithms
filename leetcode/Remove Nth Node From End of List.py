# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            # print(fast)
            fast = fast.next
            # print(slow)
            slow = slow.next
            # print(head)    
        slow.next = slow.next.next
        """ fast를 head와 같게 하고, slow는 head의 주소와 같아짐
            마지막에 slow.next = slow.next.next에서 listnode{val:3, next:{val:5, next:None}}이             되고, 마지막에 return을 호출할 때 head는 해당 slow의 주소를 참고함
        """
        return head

        # Runtime: 28 ms, faster than 93.94% of Python3 online submissions for Remove Nth Node From End of List.