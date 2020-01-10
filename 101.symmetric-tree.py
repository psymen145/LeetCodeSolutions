# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # iteratively
        q = []
        q.append(root)
        q.append(root)

        while len(q):
            t1 = q.pop(0)
            t2 = q.pop(0)
            
            if t1 == None and t2 == None:
                continue
            elif t1 is None or t2 is None:
                return False
            elif t1.val != t2.val:
                return False
            
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
            
        return True