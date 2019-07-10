class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 2 or numRows < 2:
            return s
        ret_list = [[] for i in range(numRows)]
        row = 0
        flag = 1
        for char in s:
            ret_list[row].append(char)
            if row == 0:
                flag = 1
            elif row == numRows - 1:
                flag = -1
            row += flag
        temp_list = []
        for row in ret_list:
            temp_list += row
        return ''.join(temp_list)
