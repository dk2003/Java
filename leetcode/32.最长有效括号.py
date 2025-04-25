#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        tmp = res = 0
        stack = list()
        # 栈底 存放上一次匹配失败的）的下标，-1作为哨兵下标
        stack.append(-1)
        # 每次栈底元素出栈，就表示当前次匹配到头了
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            else:
                top = stack.pop()
                length = len(stack)
                if length == 0:
                    stack.append(index)
                else:
                    tmp = index - stack[length - 1]
            res = res if res > tmp else tmp

        return res


# print(Solution().longestValidParentheses("(()"))


# @lc code=end
