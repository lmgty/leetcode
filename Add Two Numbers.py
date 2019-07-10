# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        carry = 0
        p = l1
        q = l2
        curr = dummy = ListNode(0)
        while p or q:
            if p:
                x = p.val
            else:
                x = 0
            if q:
                y = q.val
            else:
                y = 0
            total = carry + x + y
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if p:
                p = p.next
            if q:
                q = q.next

        if carry > 0:
            curr.next = ListNode(1)

        return dummy.next
