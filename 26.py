# -*- coding: UTF-8 -*-
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1

        return i+1


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    checker = Solution()
    print(checker.removeDuplicates(nums))
