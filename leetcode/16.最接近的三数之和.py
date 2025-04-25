#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        res = nums[0] + nums[1] + nums[2]

        for i in range(length):
            if nums[i]==nums[i-1] and i>0:
                continue
            left, right = i + 1, length - 1
            while left<right:
                tmp = nums[i] + nums[left] + nums[right]
                if abs(tmp-target)<abs(res-target):
                    res = tmp
                if tmp==target:
                    return target
                elif tmp>target:
                    tag=nums[right]
                    while nums[right]==tag and left<right:
                        right -= 1
                else:
                    tag=nums[left]
                    while nums[left] == tag and left < right:
                        left += 1

        return res


# print(Solution().threeSumClosest([-1, 2, 1, -4],1))

# @lc code=end
