#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        tmp = [[] for i in range(numRows)]
        carrier = 1
        index = 0
        for char in s:
            tmp[index].append(char)
            index = index + carrier if numRows != 1 else 0
            if index == numRows - 1:
                carrier = -1
            elif index == 0:
                carrier = 1
        return "".join(["".join(item) for item in tmp])


# solution = Solution()
# res = solution.convert("AB", 1)
# print(res)
# @lc code=end
