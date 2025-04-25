#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        dict_ = {
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
            quotient = num // key
            remainder = num % key
            res += f"{value}" * quotient
            num = remainder
        return res


solution=Solution()
res=solution.intToRoman(1994)
print(res)

# @lc code=end
