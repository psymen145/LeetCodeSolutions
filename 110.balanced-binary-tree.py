# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)