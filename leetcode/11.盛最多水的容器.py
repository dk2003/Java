#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left<right:
            min_height=min(height[left], height[right])
            area_cur = (right - left) * min_height
            area = area_cur if area_cur > area else area
            if height[left]<height[right]:
                while left<right and height[left]<=min_height:
                    left += 1
            else:
                while left<right and height[right]<=min_height:
                    right -= 1
        return area

solution=Solution()
res = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(res)
# @lc code=end
