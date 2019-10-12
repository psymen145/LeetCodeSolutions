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

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = m + n - 1
        p2 = m - 1
        p3 = n - 1
        
        while p2 >= 0 and p3 >= 0:
            if nums1[p2] < nums2[p3]:
                nums1[p1] = nums2[p3]
                p3 -= 1
            else:
                nums1[p1] = nums1[p2]
                p2 -= 1
            
            p1 -= 1
        
        if p3 >= 0:
            nums1[0:p3+1] = nums2[0:p3+1]
        
                    






# @lc code=end

