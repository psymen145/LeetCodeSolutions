# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # bfs
        result = []
        queue = []
        
        if not root:
            return result
        
        queue.append(root)
        
        while queue:
            lvl_list = []
            num_in_lvl = len(queue)
            
            for i in range(num_in_lvl):
                node = queue.pop(0)
                lvl_list.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(lvl_list)
            
        return result
                
            
            
        