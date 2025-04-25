#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        dict_ = {
            # key : value
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        for key in dict_:
            value = dict_[key]
            while s.startswith(value):
                res += key
                s = s[len(value) :]
        return res

solution = Solution()
res = solution.romanToInt("LVIII")
print(res)


# @lc code=end
