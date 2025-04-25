#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        tag = s[0]
        res = 0
        for index, char in enumerate(s):
            if char in ["-", "+"] and index == 0:
                continue
            elif char >= "0" and char <= "9":
                res = res * 10 + int(char)
            else:
                break
        if tag == "-":
            return -res if res <= 1 << 31 else (-1) << 31
        else:
            return res if res <= (1 << 31) - 1 else (1 << 31) - 1


# solution = Solution()
# res = solution.myAtoi("-91283472332")
# print(res)
# @lc code=end
