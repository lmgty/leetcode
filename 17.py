# -*- coding: UTF-8 -*-
class Solution:
    def letterCombinations(self, digits):
        if digits == '':
            return []
        num2char_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = ['']

        for digit in digits:
            if digit in num2char_dict.keys():
                temp = []
                for c in num2char_dict[digit]:
                    for r in res:
                        temp.append(r + c)
                res = temp
        return res


if __name__ == '__main__':
    digits = '234'
    checker = Solution()
    checker.letterCombinations(digits)
