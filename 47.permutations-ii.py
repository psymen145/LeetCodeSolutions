class Solution:
    def __init__(self):
        self.ans = []
        
    def helper(self, nums, path):
        if not nums:
            self.ans.append(path)
            return
        
        seen_children = {}
        
        for i in range(len(nums)):
            if nums[i] not in seen_children:
                seen_children[nums[i]] = True
                
                self.helper(nums[:i] + nums[i+1:], path + [nums[i]])
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.helper(nums, [])
        return self.ans