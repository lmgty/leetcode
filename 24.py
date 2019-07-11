# -*- coding: UTF-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if not head:
            return head
        current = ListNode(0)
        current.next = head
        dummy = current
        while current.next and current.next.next:
            first = current.next
            second = first.next
            temp_node = second.next

            first.next = temp_node
            second.next = first

            current.next = second
            current = first

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)

    checker = Solution()
    head = checker.swapPairs(head)
    print('head.val', head.val)

    while True:
        if head.next:
            print(head.val)
            head = head.next
        else:
            print(head.val)
            break
