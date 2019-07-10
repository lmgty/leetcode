# -*- coding: UTF-8 -*-
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        if length == 1:
            return strs[0]
        elif length == 0:
            return ''
        prefix = self.longest_prefix(strs[0], strs[1])
        for i in range(2, len(strs)):
            prefix = self.longest_prefix(prefix, strs[i])
        return prefix

    def longest_prefix(self, str1, str2):
        length1 = len(str1)
        length2 = len(str2)
        prefix = ''
        for i in range(min(length1, length2)):
            if str1[i] == str2[i]:
                prefix += str1[i]
            else:
                break
        return prefix
