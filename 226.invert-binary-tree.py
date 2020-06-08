# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # use bfs to invert tree
        # implemented with a queue
        '''
        if not root:
            return
        
        q = [root]
        
        while q:
            n = q.pop(0)
            
            tmp = n.left
            n.left = n.right
            n.right = tmp
            
            # add to queue
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
                
        return root
        '''
            
        # recursive approach
        if root is None:
            return
        
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
            
            