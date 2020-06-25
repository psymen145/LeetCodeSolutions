# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## NOTE FOR BST, IF ALREADY TOO SMALL ( < L ), YOU CAN IGNORE ALL LEFT SUBTREES. VICE VERSA FOR RIGHT.
    def _rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return
            
            if node.val <= R and node.val >= L:
                self.ans += node.val
            
            if node.val >= L:
                dfs(node.left)
            
            if node.val <= R:
                dfs(node.right)
            
        dfs(root)
        return self.ans
    
    def rangeSumBST(self, root, L, R):
        ans = 0
        
        q = [root]
        
        while q:
            node = q.pop(0)
            
            if not node:
                continue
                
            if node.val >= L:
                q.append(node.left)
                
            if node.val <= R:
                q.append(node.right)
                
            if node.val <= R and node.val >= L:
                ans += node.val
                
        return ans
            
                
                
        
        
        