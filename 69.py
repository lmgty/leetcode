# -*- coding: UTF-8 -*-
class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        left = 1
        right = x // 2

        while left < right:
            mid = (left + right + 1) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid

        return left


if __name__ == '__main__':
    checker = Solution()
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in nums:
        print(checker.mySqrt(num))
