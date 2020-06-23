# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        
    def solve(self, node):
        # return 0 , 1 , 2 
        if not node:
            return 'covered no camera'
               
        l_val, r_val = self.solve(node.left), self.solve(node.right)
            
        if l_val == 'to be covered' or r_val == 'to be covered':
            self.ans += 1
            return 'covering'
        
        if l_val == 'covering' or r_val == 'covering':
            return 'covered no camera'
        else:
            return 'to be covered'
        
        
    def minCameraCover(self, root: TreeNode) -> int:
        
        tmp_ans = (self.solve(root) == 'to be covered')
        
        return tmp_ans + self.ans