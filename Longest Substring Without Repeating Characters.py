# -*- coding: UTF-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest_str = s[0]
        max_len = 1

        start = 0
        end = 1
        length = len(s)
        for i in range(1, length):
            if s[i] in s[start:end]:
                start = s[start:end].index(s[i]) + 1 + start
            end = i + 1
            if end - start >= max_len:
                max_len = end - start
                longest_str = s[start:end]
                max_len = len(longest_str)

        return max_len