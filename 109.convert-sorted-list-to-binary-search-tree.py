# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertToList(self, node):  
        l = []
        while node:
            l.append(node.val)
            node = node.next
            
        return l
    
    def helper(self, lst):
        if not lst:
            return None
        
        mid = len(lst) // 2
        
        node = TreeNode(lst[mid])
        node.left = self.helper(lst[:mid])
        node.right = self.helper(lst[mid+1:])
        return node
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        l = self.convertToList(head)
        return self.helper(l)