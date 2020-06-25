class Solution:
    def __init__(self):
        self.ans = []
        
    def helper(self, nums, path):
        if not nums:
            self.ans.append(path)
            return
            
        for i in range(len(nums)):
            self.helper(nums[:i] + nums[i+1:], path + [nums[i]])
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, [])
        
        return self.ans
        
                