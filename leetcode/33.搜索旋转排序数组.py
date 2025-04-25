from typing import List

#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#


# @lc code=start
class Solution:
    def search_binary(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            tmp = nums[mid]
            if tmp == target:
                return mid
            elif tmp < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            tmp_1 = nums[mid]
            if tmp_1 == target:
                return mid
            if tmp_1 >= nums[0] and tmp_1 <= nums[length - 1]:
                return self.search_binary(nums, 0, length - 1, target)
            if tmp_1 >= nums[0] and tmp_1 > nums[length - 1]:
                tmp_2 = self.search_binary(nums, left, mid - 1, target)
                if tmp_2 != -1:
                    return tmp_2
                else:
                    left = mid + 1
            elif tmp_1 < nums[0] and tmp_1 <= nums[length - 1]:
                tmp_3 = self.search_binary(nums, mid + 1, right, target)
                if tmp_3 != -1:
                    return tmp_3
                else:
                    right = mid - 1
        return -1


# print(Solution().search([3, 1], 0))
# @lc code=end
