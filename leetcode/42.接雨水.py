from typing import List

#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # res表示雨水量
        res = 0
        length = len(height)
        # 一个单调递减栈，存放的是下标
        stack = []
        for i in range(0, length):
            # 满足单调递减，则入栈
            if len(stack) == 0 or height[stack[-1]] >= height[i]: # 利用[-1]快速获得最后一个元素
                # 将下标入栈
                stack.append(i)
            else:
                # 将不满足递减的栈顶元素全部出栈
                while len(stack) >= 1 and height[stack[-1]] < height[i]:
                    # 每出栈一个元素，就增加一些雨水的体积

                    # 获取底边高度
                    lower = height[stack.pop()]
                    # 若底边出栈之后，左边界为空，无法蓄水，直接跳出
                    if len(stack) == 0:
                        break
                    # 有效高度取决于短板效应
                    higher = min(height[stack[-1]], height[i])
                    # 该蓄水区的宽度
                    width = i - stack[-1] - 1
                    # 该蓄水区的体积
                    res += (higher - lower) * width
                # 入栈
                stack.append(i)
        return res


# print(Solution().trap([4, 2, 0, 3, 2, 5]))


# @lc code=end
