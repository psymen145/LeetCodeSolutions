# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # bfs -> queue
        if not root:
            return True
        
        t_val = root.val
        q = [root]
        
        while q:
            node = q.pop(0)
            
            if node:
                q.append(node.left)
                q.append(node.right)
            
                if t_val != node.val:
                    return False
            
        return True
            
        
    def _isUnivalTree(self, root: TreeNode) -> bool:
        # dfs -> recursion
        if not root:
            return True
        
        if root.right and root.right.val != root.val:
            return False
        
        if root.left and root.left.val != root.val:
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        