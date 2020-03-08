# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.best = 0
        
        def depth(root):
            if root is None:
                return 0
            
            l_length = depth(root.left)
            r_length = depth(root.right)
            self.best = max(l_length + r_length, self.best)
            return 1 + max(l_length, r_length)
        
        depth(root)
        return self.best
            
            