from typing import Optional
#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        prev = next = head
        for i in range(k - 1):
            if next.next:
                next = next.next
            else:
                return head
        next_prev = next.next
        cur=prev
        while cur!=next:
            tag=cur.next
            cur.next=next.next
            next.next=cur
            cur = tag
        prev.next = self.reverseKGroup(next_prev, k)
        return next


# @lc code=end
