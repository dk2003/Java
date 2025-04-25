from typing import Optional

#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def travel(node, n):
            if node == None:
                return 0
            last_k = travel(node.next, n) + 1
            if last_k == n + 1:
                node.next = node.next.next
            return last_k
        last_k = travel(head, n)
        if last_k == n:
            return head.next
        else: 
            return head


# @lc code=end
