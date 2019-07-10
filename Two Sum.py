# -*- coding: UTF-8 -*-
class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        my_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if my_map.get(diff) != i and diff in my_map:
                return my_map[diff], i
            my_map[nums[i]] = i