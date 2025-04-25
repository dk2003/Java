from typing import List

#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tmp_1 = set()
        tmp_2 = set()
        tmp_3 = [set() for i in range(0, 9)]
        for i in range(0, 9):
            tmp_1.clear()
            tmp_2.clear()
            for j in range(0, 9):
                tmp_4 = 3 * (i // 3) + (j // 3)
                if (
                    (board[i][j] in tmp_1 and board[i][j] != ".")
                    or (board[j][i] in tmp_2 and board[j][i] != ".")
                    or (board[i][j] in tmp_3[tmp_4] and board[i][j] != ".")
                ):
                    return False
                else:
                    tmp_1.add(board[i][j])
                    tmp_2.add(board[j][i])
                    tmp_3[tmp_4].add(board[i][j])
        return True


# print(
#     Solution().isValidSudoku(
#         [
#             ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#             [".", "9", "8", ".", ".", ".", ".", "6", "."],
#             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#             [".", "6", ".", ".", ".", ".", "2", "8", "."],
#             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#             [".", ".", ".", ".", "8", ".", ".", "7", "9"],
#         ]
#     )
# )

# @lc code=end
