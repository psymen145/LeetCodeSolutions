# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    
    def helper(self,root):
        if not root:
            return 0
        
        l = self.helper(root.left)
        r = self.helper(root.right)

        excess = l + r + root.val - 1

        self.ans += abs(excess)
        
        return excess

    def distributeCoins(self, root: TreeNode) -> int:
        self.helper(root)
        return self.ans