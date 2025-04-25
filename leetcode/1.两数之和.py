#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#


# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)

        # 使用哈希表以实现快速查找
        d = dict()
        for i in range(0, length):
            tmp = target - nums[i]
            if d.has_key(tmp):
                return [i, d[tmp]]
            else:
                d[nums[i]] = i

# @lc code=end
