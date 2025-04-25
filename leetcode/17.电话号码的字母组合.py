#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    dict_ = ["","",'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    def letterCombinations(self, digits: str) -> list[str]:
        res, length = [], len(digits)

        if length == 0:
            return []

        path=['']*length

        def dfs(i):
            if i==length:
                res.append("".join(path))
                return
            else:
                for char in self.dict_[int(digits[i])]:
                    path[i]=char
                    dfs(i + 1)
        dfs(0)
        return res


print(Solution().letterCombinations(""))
# @lc code=end
