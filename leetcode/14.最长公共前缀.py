#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_len = min(map(lambda x: len(x), strs))
        res = ""
        for i in range(min_len):
            set_ = {str[i] for str in strs}
            if len(set_) == 1:
                res += set_.pop()
            else:
                break
        return res


solution=Solution()
res = solution.longestCommonPrefix(["flower", "flow", "flight"])
print(res)
# @lc code=end
