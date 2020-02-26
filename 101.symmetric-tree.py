# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root and root.left and root.right:
            return self.isMirror(root.left, root.right)
        elif not root or (not root.left and not root.right):
            return True
        else:
            return False
    
    def isMirror(self, t1, t2):
        if (t1 is None and t2 is not None) or (t1 is not None and t2 is None):
            return False
        if t1 is None and t2 is None:
            return True
        
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)

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