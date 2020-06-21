# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMax(self, nums):
        max_num = max(nums)
        
        max_index = 0
        for i in range(len(nums)):
            if nums[i] == max_num:
                max_index = i
                
        return (max_num, max_index)
        
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        max_num, max_index = self.findMax(nums)
        
        node = TreeNode(max_num)
        
        node.left = self.constructMaximumBinaryTree(nums[:max_index])
        node.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        
        return node
                