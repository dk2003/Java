from typing import List

#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        slow = 0
        for fast in range(length):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


# print(Solution().removeElement([3, 2, 2, 3], 3))

# @lc code=end
