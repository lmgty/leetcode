# -*- coding: UTF-8 -*-
class Solution:
    def searchInsert(self, nums, target):
        length = len(nums)
        if length == 0:
            return 0
        if target > nums[-1]:
            return length

        left = 0
        right = length - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    nums = [1, 2, 3, 5, 6, 8, 9]
    target = 2
    checker = Solution()
    print(checker.searchInsert(nums, target))
