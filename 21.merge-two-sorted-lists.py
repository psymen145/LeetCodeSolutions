#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
                
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
                
        return head.next
        
                    






# @lc code=end

