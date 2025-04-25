#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = 1
        maxStart = 0
        length=len(s)
        dp = [[1 if i == j else 0 for j in range(0, length)] for i in range(0, length)]
        for index in range(0, length):
            if index == 0:
                continue
            else:
                for j in range(0, index):
                    if dp[j][index - 1] == 1:
                        if j == index - 1 and s[j] == s[index]:
                            dp[j][index] = 1
                            if index - j + 1 > max:
                                max = index - j + 1
                                maxStart = j
                        if j == 0:
                            continue
                        if s[j - 1] == s[index]:
                            dp[j - 1][index] = 1
                            if index - j + 2 > max:
                                max = index - j + 2
                                maxStart = j - 1
        return s[maxStart : maxStart + max : 1]


# solution = Solution()
# res = solution.longestPalindrome("babad")
# print(res)
# @lc code=end
