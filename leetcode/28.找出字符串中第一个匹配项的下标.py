#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#


# @lc code=start
class Solution:

    def getNext(self, needle):
        length = len(needle)
        next = [0] * (length if length >= 2 else 2)
        next[0], next[1] = -1, 0
        for i in range(2, length):
            k = next[i - 1]
            while k != -1 and needle[k] != needle[i - 1]:
                k = next[k]
            next[i] = k + 1
        return next

    def getNextVal(self,needle):
        next=self.getNext(needle)
        for i in range(2,len(next)):
            tmp=next[i]
            while needle[i] == needle[tmp] and tmp >= 0:
                tmp = next[tmp]
            next[i] = tmp
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        len1, len2 = len(haystack), len(needle)
        next = self.getNextVal(needle)
        i = j = 0
        while i < len1:
            while i < len1 and j < len2:
                if haystack[i] == needle[j] or j == -1:
                    i += 1
                    j += 1
                else:
                    j = next[j]
                    break
            if j == len2:
                return i - len2
        return -1


print(Solution().strStr("mississippi", "issip"))
# @lc code=end
