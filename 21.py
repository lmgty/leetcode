# -*- coding: UTF-8 -*-
class Solution:
    def generateParenthesis(self, n):
        res = []
        s = ''
        self.recursion(s, res, n, n)
        return res

    def recursion(self, s, res, left, right):
        if left == right == 0:
            res.append(s)
        if left > 0:
            self.recursion(s + '(', res, left - 1, right)
        if right > left:
            self.recursion(s + ')', res, left, right - 1)


if __name__ == '__main__':
    n = 3

    checker = Solution()
    print(checker.generateParenthesis(n))
