#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#


# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) == (divisor > 0)
        dividend, divisor, res = abs(dividend), abs(divisor), 0

        # 依次确定最高位到最低位商几
        for i in range(32, -1, -1):
            if divisor << i <= dividend:
                res += 1 << i
                dividend -= divisor << i
        return min(res, (1 << 31) - 1) if positive else max(-1 << 31, -res)

print(Solution().divide(-2147483648,-1))
# @lc code=end
