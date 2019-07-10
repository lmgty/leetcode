# -*- coding: UTF-8 -*-
class Solution:
    def reverse(self, x: int) -> int:
        flag = 1 if x > 0 else -1
        x = x * flag
        temp_str = str(x)[::-1]
        new_num = flag * int(temp_str)
        if new_num > 2**31 - 1 or new_num < -2**31:
            return 0
        return new_num