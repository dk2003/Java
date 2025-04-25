#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        len_nums=len(nums)
        nums=sorted(nums)
        for i in range(len_nums):
            # 去重，若当前i指向的数字不变，那么直接跳过
            if nums[i] == nums[i - 1] and i != 0:
                continue

            left = i + 1
            right = len_nums - 1
            while left<right:
                tmp=nums[i]+nums[left]+nums[right]
                if tmp<0:
                    left+=1
                elif tmp>0:
                    right-=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    tag=nums[left]

                    # 去重，移动左指针，直到左指针指向的值发生变化
                    while nums[left] == tag and left < right:
                        left+=1
        return res

res = Solution().threeSum([-1, 0, 1, 2, -1, -4])
[-4, -1, -1, 0, 1, 2]
print(res)


# @lc code=end
