# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    def __init__(self):
        self.ret = []
        
    def trav(self, node):
        if node is None:
            return
        
        self.trav(node.left)
        self.ret.append(node.val)
        self.trav(node.right)
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.trav(root)
        
        return self.ret
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stck = [(root, False)]
        res = []
        
        while stck:
            node, visited = stck.pop()
            if node:
                if visited:
                    res.append(node.val)
                else:
                    stck.append((node.right, False))
                    stck.append((node, True))
                    stck.append((node.left, False))
                    
        return res

