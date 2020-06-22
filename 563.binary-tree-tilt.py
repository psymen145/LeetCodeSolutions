# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total_tilt = 0
        
    def helper(self, root):
        if not root:
            return 0
        
        left_val = 0
        if root.left:
            left_val = self.helper(root.left)
        
        right_val = 0
        if root.right:
            right_val = self.helper(root.right)
            
        self.total_tilt += abs(left_val - right_val)
        
        return root.val + left_val + right_val
        
    def findTilt(self, root: TreeNode) -> int:
        self.helper(root)
        return self.total_tilt