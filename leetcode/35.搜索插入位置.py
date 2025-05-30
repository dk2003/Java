from typing import List

#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            tmp = nums[mid]
            if tmp == target:
                return mid
            elif tmp < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


# @lc code=end
