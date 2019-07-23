# -*- coding: UTF-8 -*-
class Solution:
    def isValidSudoku(self, board):
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    boxes_index = (i // 3) * 3 + j // 3

                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[boxes_index][num] = boxes[boxes_index].get(num, 0) + 1

                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[boxes_index][num] > 1:
                        return False
        return True


if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", "5", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    checker = Solution()
    print(checker.isValidSudoku(board))
