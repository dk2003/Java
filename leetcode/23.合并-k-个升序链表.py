from typing import Optional, List
import heapq

#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res =cur= ListNode()
        heap = [
            (list_node.val, list_id, list_node)
            for list_id, list_node in enumerate(lists)
            if list_node
        ]
        heapq.heapify(heap)
        while heap:
            value, list_id, list_node = heapq.heappop(heap)
            cur.next = list_node
            cur = cur.next
            if list_node.next != None:
                next_value = list_node.next.val
                heapq.heappush(heap, (next_value, list_id, list_node.next))
        return res.next

# @lc code=end
