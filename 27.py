# -*- coding: UTF-8 -*-
class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)


if __name__ == '__main__':
    haystack = "wwwaaaaa"
    needle = "aa"
    checker = Solution()
    print(checker.strStr(haystack, needle))
