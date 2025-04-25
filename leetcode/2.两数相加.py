#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         i = l1
#         j = l2
#         carrier = 0
#         # res是哨兵节点
#         res = node = ListNode()
#         while i or j:
#             tmp = (i.val if i else 0) + (j.val if j else 0) + carrier
#             # 表示本位和
#             cur = tmp % 10
#             # 表示来自低位的进位
#             carrier = tmp // 10
#             # // 表示取整除法 9//4=2 9.0//4.0=2.0
#             if i:
#                 i = i.next
#             if j:
#                 j = j.next
#             node.next = ListNode(cur)
#             node = node.next
#         if carrier == 1:
#             node.next = ListNode(1)
#         # 返回哨兵节点的下一个
#         return res.next


def add(node1, node2, node, carrier):
    if node1 or node2 or carrier:
        num1 = node1.val if node1 else 0
        num2 = node2.val if node2 else 0
        tmp = num1 + num2 + carrier
        node.next = ListNode(tmp % 10)
        add(
            node1.next if node1 else None,
            node2.next if node2 else None,
            node.next,
            tmp // 10,
        )
    else:
        return


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = node = ListNode()
        add(l1, l2, node, 0)
        return res.next


# @lc code=end
