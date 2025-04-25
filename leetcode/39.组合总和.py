from typing import List

#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []
        length = len(candidates)
        minValue = min(candidates)
        # candidates.sort()

        def dfs(i, remain):
            if remain == 0:
                res.append([*tmp])
                return
            if remain < minValue:
                return

            for index in range(i, length):
                num = candidates[index]
                if num > remain:
                    continue
                else:
                    tmp.append(num)
                    dfs(index, remain - num)
                    tmp.pop()

        dfs(0, target)
        return res


# print(Solution().combinationSum([8, 7, 4, 3], 11))

# @lc code=end
