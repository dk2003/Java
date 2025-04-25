from typing import Optional

#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head=head.next
        head.next=self.swapPairs(new_head.next)
        new_head.next = head
        return new_head


# print(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))


# @lc code=end
