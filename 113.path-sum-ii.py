# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
      
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.ans = []
        tmp = []
        self.dfs(root, sum, tmp)
        return self.ans
        
    def dfs(self, root, sum, lst):
        if root is None:
            return 

        if root.left is None and root.right is None and (sum - root.val == 0):
            lst.append(root.val)
            self.ans.append(lst)
            return
            
        if root.left:
            self.dfs(root.left, sum - root.val, lst + [root.val])
        if root.right:
            self.dfs(root.right, sum - root.val, lst + [root.val])