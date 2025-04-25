#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#


# @lc code=start
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # 先排序，方便使用双指针和去重
        nums.sort()
        length = len(nums)
        res = []
        for i in range(length-3):
            # 去重关键步骤：若nums[i]和nums[i-1]相同，则直接跳过
            # 因为满足包含nums[i]的四元组，肯定已经含于nums[i-1]的四元组
            if nums[i]==nums[i-1] and i>0:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
                break
            if nums[i]+nums[length-1]+nums[length-2]+nums[length-3]<target:
                continue
            for j in range(i + 1, length - 2):
                # 去重关键步骤：若nums[j]和nums[j-1]相同，则直接跳过
                if nums[j] == nums[j - 1] and j > i + 1:
                    continue
                if nums[j]+nums[j+1]+nums[j+2]>target-nums[i]:
                    break
                if nums[j] + nums[length - 1] + nums[length - 2] < target - nums[i]:
                    continue
                front, end = j + 1, length - 1
                while front < end:
                    sum = nums[i] + nums[j] + nums[front] + nums[end]
                    if sum > target:
                        end -= 1
                    elif sum < target:
                        front += 1
                    else:
                        res.append([nums[i], nums[j], nums[front], nums[end]])
                        flag=nums[front]
                        while front < end and nums[front] == flag:
                            front += 1
        return res


print(Solution().fourSum([2,2,2,2,2], 8))

# @lc code=end
