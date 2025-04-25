#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# @lc code=start
class Solution:
    dict_ = dict()
    def isMatch(self, s: str, p: str) -> bool:
        key = f"{s},{p}"

        if key in self.dict_:
            return self.dict_[key]

        if s==p:
            return True

        equalFirst = len(p) > 0 and len(s) > 0 and (p[0] in (s[0], "."))
        ignoreFirst=len(p)>1 and p[1]=='*'
        if equalFirst and not ignoreFirst:
            self.dict_[key] = self.isMatch(s[1:], p[1:])
        elif not equalFirst and ignoreFirst:
            self.dict_[key] = self.isMatch(s, p[2:])
        elif not equalFirst and not ignoreFirst:
            self.dict_[key] = False
        elif equalFirst and ignoreFirst:
            self.dict_[key] = self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)

        return self.dict_[key]

solution = Solution()
res = solution.isMatch("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*")
print(res)

# @lc code=end
