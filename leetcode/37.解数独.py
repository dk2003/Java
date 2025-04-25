from typing import List

#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_remian = [
            set(["1", "2", "3", "4", "5", "6", "7", "8", "9"]) for i in range(0, 9)
        ]
        column_remain = [
            set(["1", "2", "3", "4", "5", "6", "7", "8", "9"]) for i in range(0, 9)
        ]
        square_remain = [
            set(["1", "2", "3", "4", "5", "6", "7", "8", "9"]) for i in range(0, 9)
        ]

        for i in range(0, 9):
            for j in range(0, 9):
                square_index = 3 * (i // 3) + (j // 3)
                tmp = board[i][j]
                if tmp != ".":
                    row_remian[i].remove(tmp)
                    column_remain[j].remove(tmp)
                    square_remain[square_index].remove(tmp)

        tmp = []
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    tmp.append([i, j])
        length = len(tmp)

        def dfs(high):
            if high == length:
                return True
            i, j = tmp[high]
            square_index = 3 * (i // 3) + (j // 3)
            remain = row_remian[i] & column_remain[j] & square_remain[square_index]
            if len(remain) == 0:
                return False
            else:
                for ele in remain:
                    board[i][j] = ele
                    row_remian[i].remove(ele)
                    column_remain[j].remove(ele)
                    square_remain[square_index].remove(ele)
                    res = dfs(high + 1)
                    if res == False:
                        row_remian[i].add(ele)
                        column_remain[j].add(ele)
                        square_remain[square_index].add(ele)
                    else:
                        return True
                board[i][j] = "."
                return False

        dfs(0)

#         for i in range(0, 9):
#             for j in range(0, 9):
#                 print(board[i][j], end=" ")
#             print("\n")


# Solution().solveSudoku(
#     [
#         [".", ".", "9", "7", "4", "8", ".", ".", "."],
#         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
#         [".", "2", ".", "1", ".", "9", ".", ".", "."],
#         [".", ".", "7", ".", ".", ".", "2", "4", "."],
#         [".", "6", "4", ".", "1", ".", "5", "9", "."],
#         [".", "9", "8", ".", ".", ".", "3", ".", "."],
#         [".", ".", ".", "8", ".", "3", ".", "2", "."],
#         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
#         [".", ".", ".", "2", "7", "5", "9", ".", "."],
#     ]
# )

# @lc code=end
