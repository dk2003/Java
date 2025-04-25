from typing import List

#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length
        for i in range(length - 2, -1, -1):
            tmp = temperatures[i]
            next_pos = i + 1
            if tmp < temperatures[next_pos]:
                res[i] = 1
                continue

            while tmp >= temperatures[next_pos]:
                distance = res[next_pos]
                if distance == 0:
                    res[i] = 0
                    break
                next_pos += distance
            if distance != 0:
                res[i] = next_pos - i
        return res


# print(Solution().dailyTemperatures([30, 60, 90,100]))

# @lc code=end
