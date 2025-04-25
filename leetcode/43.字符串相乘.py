#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        length1, length2 = len(num1), len(num2)
        res = [0] * (length1 + length2)

        for index_1, num_str1 in enumerate(num1[::-1]):
            position = length2 + length1 - 1 - index_1
            for index_2, num_str2 in enumerate(num2[::-1]):
                position_cur = position - index_2
                mul = int(num_str1) * int(num_str2)
                res[position_cur] += mul

        for i in range(length1 + length2-1, 0, -1):
            tmp = res[i]
            res[i] = tmp % 10
            res[i - 1] += tmp // 10

        return "".join(map(str, res)).lstrip("0")


# print(Solution().multiply("123", "456"))

# @lc code=end
