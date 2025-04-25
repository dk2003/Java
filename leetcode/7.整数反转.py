#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        tmp = abs(x)
        while tmp >= 1:
            res = res * 10 + tmp % 10
            tmp = (tmp - tmp % 10) // 10
        if res >= 2**31 - 1:
            return 0
        return res if x > 0 else -res


# solution = Solution()
# res = solution.reverse(123)
# print(res)


# @lc code=end
