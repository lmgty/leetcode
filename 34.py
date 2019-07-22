# -*- coding: UTF-8 -*-
class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        length = len(nums)
        res = []
        left = 0
        right = length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return [-1, -1]
        else:
            res.append(left)

        left = 0
        right = length - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        if nums[left] != target:
            return [-1, -1]
        else:
            res.append(left)
        return res


if __name__ == '__main__':
    nums = [5, 6, 7, 8, 8, 8, 8, 8, 10]
    target = 8
    checker = Solution()
    print(checker.searchRange(nums, target))
