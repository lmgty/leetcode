# -*- coding: UTF-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        before_delete_node = tail_node = dummy
        for i in range(n+1):
            tail_node = tail_node.next
        while tail_node:
            tail_node = tail_node.next
            before_delete_node = before_delete_node.next
        before_delete_node.next = before_delete_node.next.next

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)

    checker = Solution()
    head = checker.removeNthFromEnd(head, 1)
    print('head.val', head.val)

    while True:
        if head.next:
            print(head.val)
            head = head.next
        else:
            print(head.val)
            break
