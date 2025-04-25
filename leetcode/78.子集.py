#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res, path = [], []
        length = len(nums)

        # 深度优先：先序遍历
        def dfs(i):
            if i == length + 1:
                return
            res.append(path.copy())

            for index in range(i,length):
                path.append(nums[index])
                dfs(index + 1)
                path.pop()

        dfs(0)

        return res

print(Solution().subsets([1,2,3]))

# @lc code=end
