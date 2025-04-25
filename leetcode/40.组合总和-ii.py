from typing import List

#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#


# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []
        length = len(candidates)
        candidates.sort()


        def dfs(i, remain):
            if remain == 0:
                res.append([*tmp])
                return
            if remain < candidates[0]:
                return

            for index in range(i + 1, length):
                num = candidates[index]
                if index >= 1 and num == candidates[index - 1] and index-1 >= i + 1:
                    continue
                if num > target:
                    break
                else:
                    tmp.append(num)
                    dfs(index, remain - num)
                    tmp.pop()

        dfs(-1, target)
        return res


print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
# @lc code=end
