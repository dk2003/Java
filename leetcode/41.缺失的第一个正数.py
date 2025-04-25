from typing import List

#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#


# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for index, num in enumerate(nums):
            if num <= 0 or num > length:
                nums[index] = length + 1

        for index, num in enumerate(nums):
            tmp = abs(num)
            if tmp <= length:
                if nums[tmp - 1] > 0:
                    nums[tmp - 1] = -nums[tmp - 1]

        for index, num in enumerate(nums):
            if num > 0:
                return index + 1

        return length + 1


# print(Solution().firstMissingPositive([1]))


# @lc code=end
