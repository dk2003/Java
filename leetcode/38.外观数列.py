#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for i in range(0, n - 1):
            times = 1
            index = 1
            tmp = ""
            while index <= len(res):
                if index == len(res) or res[index] != res[index - 1]:
                    tmp += f"{times}{res[index-1]}"
                    times = 1
                else:
                    times += 1
                index += 1
            res = tmp
        return res


# print(Solution().countAndSay(5))


# @lc code=end
