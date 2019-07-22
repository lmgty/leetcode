# -*- coding: UTF-8 -*-
class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if nums[left] == target:
            return left
        else:
            return -1



if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    checker = Solution()
    print(checker.search(nums, target))
