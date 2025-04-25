from typing import List

#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#


# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length=len(nums)
        i = length - 1
        while i-1>=0 and nums[i-1]>=nums[i]:
            i-=1
        if i == 0:
            self.reverse(0,length-1,nums)
            return nums

        tag = length - 1
        for j in range(i,length):
            if nums[j]<=nums[i-1]:
                tag = j - 1
                break
        nums[i-1],nums[tag]=nums[tag],nums[i-1]
        self.reverse(i, length - 1, nums)
        return nums

    def reverse(self,i,j,nums):
        if i < 0 or j > len(nums) - 1 or i > j:
            return False
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j -= 1
        return True


# print(Solution().nextPermutation([5,1,1]))

# @lc code=end
