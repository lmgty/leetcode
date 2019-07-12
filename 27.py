# -*- coding: UTF-8 -*-
class Solution:
    def removeElement(self, nums, val):
        p = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p


if __name__ == '__main__':
    nums = [1]
    val = 1
    checker = Solution()
    print(checker.removeElement(nums, val))
    print(nums)
