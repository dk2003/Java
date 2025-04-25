#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = 0
        y=x
        while x >= 1:
            tmp = tmp * 10 + x % 10
            x = (x - x % 10) // 10
        return tmp == y
# @lc code=end
