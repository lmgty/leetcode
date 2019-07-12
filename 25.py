# -*- coding: UTF-8 -*-

# ——————————暂时没写出来——————————

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = new = old = head
        cnt = 1
        while old:
            old = old.next
            cnt += 1
            if cnt % k == 0:
                temp = old.next
                dummy.next = self.reverse_node(new, k)
                new = old
                old = temp

        return dummy.next

    def reverse_node(self, head, k):
        dummy = ListNode(0)
        dummy.next = new = head
        old = new.next

        for _ in range(k-1):
            temp = old.next
            old.next = new
            new = old
            old = temp
        dummy.next.next = old
        print('new.val:', new.val)
        return new


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)
    k = 4

    checker = Solution()
    head = checker.reverseKGroup(head, 2)
    # print('head.val', head.val)

    while True:
        if head.next:
            print(head.val)
            head = head.next
        else:
            print(head.val)
            break
