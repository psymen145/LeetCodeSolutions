# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.hashtbl = {}
        
    def dfs(self, node, lvl, node_id) -> int:
        # the trick is to give each node a position value
        # width at each level would be R - L + 1
        if not node:
            return
        
        if lvl not in self.hashtbl:
            # found left most node
            self.hashtbl[lvl] = [node_id, None]
        else:
            # already found left most node
            self.hashtbl[lvl][1] = node_id
            
        self.dfs(node.left, lvl + 1, node_id * 2)
        self.dfs(node.right, lvl + 1, node_id * 2 + 1)
        
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        self.dfs(root, 1, 1)
        
        # find width of each row
        max_width = 1
        for row, widths in self.hashtbl.items():
            left, right = widths[0], widths[1]
            
            if left and right:
                row_width = right - left + 1
                
                if row_width > max_width:
                    max_width = row_width
                    
        return max_width
        
        