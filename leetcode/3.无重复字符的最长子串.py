#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#

# @lc code=start


# 法1：动态规划
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        tmp = [0] * len(s)

        for index, item in enumerate(s):
            tmp[index] = 1
            if index != 0:
                for index1 in range(index - 1, index - 1 - tmp[index - 1], -1):
                    if s[index1] != item:
                        tmp[index] += 1
                    else:
                        break
            max = tmp[index] if tmp[index] > max else max
        return max


# 法2：使用哈希表优化动态规划中的查找过程
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        tmp = [0] * len(s)

        d = dict()

        for index, item in enumerate(s):
            tmp[index] = 1
            if index != 0:
                if item in d and d[item] >= index - tmp[index - 1]:
                    tmp[index] = index - d[item]
                else:
                    tmp[index] = tmp[index - 1] + 1

            d[item] = index
            max = tmp[index] if tmp[index] > max else max
        return max


# 滑动窗口优化，使用start变量记录最长无重复子串的起始位置
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        start = 0
        d = dict()

        for index, item in enumerate(s):
            if item in d and d[item] >= start:
                start = d[item] + 1
            d[item] = index
            tmp = index - start + 1
            max = tmp if tmp > max else max
        return max


# @lc code=end
