#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#


# @lc code=start
# 回溯模板
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []
        def add(already_left_num, remain_left_num):
            if already_left_num == n and remain_left_num == 0:
                res.append("".join(path))
                return
            if already_left_num < n:
                path.append("(")
                add(already_left_num + 1, remain_left_num + 1)
                path.pop()
            if remain_left_num > 0:
                path.append(")")
                add(already_left_num, remain_left_num - 1)
                path.pop()

        add(0, 0)
        return res


# print(len(Solution().generateParenthesis(4)))

# @lc code=end
