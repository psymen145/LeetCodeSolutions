# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """RECURSIVE APPROACH"""
    def helper(self, prev, curr):
        if curr is None:
            return prev
        
        tmp = curr.next
        curr.next = prev
        return self.helper(curr, tmp)

    def reverseList(self, head: ListNode) -> ListNode:
        return self.helper(None, head)
    
    """ ITERATIVE APPROACH
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
    """