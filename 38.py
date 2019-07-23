# -*- coding: UTF-8 -*-
class Solution:
    def countAndSay(self, n):
        new_str = '1'

        for i in range(n-1):
            new_str = self.count_num(new_str)
        return new_str

    def count_num(self, new_str):
        temp_c = new_str[0]
        cnt = 0
        temp_str = ''
        for c in new_str:
            if c == temp_c:
                cnt += 1
            else:
                temp_str = temp_str + str(cnt) + temp_c
                cnt = 1
                temp_c = c
        temp_str = temp_str + str(cnt) + temp_c
        return temp_str



if __name__ == '__main__':
    n = 1
    checker = Solution()
    print(checker.countAndSay(n))
