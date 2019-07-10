# -*- coding: UTF-8 -*-
class Solution:
    def isValid(self, s):
        if s == '':
            return True
        stack = []
        left_dict = {
            '[': ']',
            '(': ')',
            '{': '}',
        }
        right_dict = {
            ']': '[',
            ')': '(',
            '}': '{',
        }
        for char in s:
            if char in left_dict:
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()
                if right_dict[char] != top:
                    return False
        return not stack


if __name__ == '__main__':
    s = "()[]"
    checker = Solution()
    print(checker.isValid(s))

    print(not [])
