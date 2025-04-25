from typing import List

#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lc code=start
class Solution:
    def searchBinary(self, nums: List[int], target: int, left, right) -> List[int]:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        tmp = self.searchBinary(nums, target, 0, len(nums) - 1)
        if tmp == -1:
            return [-1, -1]
        else:
            tmp_left = tmp_right = tmp
            while True:
                tmp_1 = self.searchBinary(nums, target, 0, tmp_left - 1)
                if tmp_1 != -1:
                    tmp_left = tmp_1
                else:
                    break

            while True:
                tmp_2 = self.searchBinary(nums, target, tmp_right + 1, length - 1)
                if tmp_2 != -1:
                    tmp_right = tmp_2
                else:
                    break

            return [tmp_left, tmp_right]


# print(Solution().searchRange([5, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9], 9))
# @lc code=end
