#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#


# @lc code=start


# 法一：将两个数组归并到一个新的数组
# 时间复杂度：o(m+n)
# 空间复杂度：o(m+n)
# 法一：双指针寻找中间的数，时间复杂度  o(m+n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        length1 = len(nums1)
        length2 = len(nums2)
        length = length1 + length2
        nums3 = []
        i = j = 0
        while i < length1 or j < length2:
            if i == length1:
                nums3.extend(nums2[j::])
                break
            if j == length2:
                nums3.extend(nums1[i::])
                break
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        if length % 2 == 0:
            return (nums3[length // 2 - 1] + nums3[length // 2]) / 2
        else:
            return nums3[length // 2]


solution = Solution()
res = solution.findMedianSortedArrays([1,2], [3,4])
print(res)
# @lc code=end
