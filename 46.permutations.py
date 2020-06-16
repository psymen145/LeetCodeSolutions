class Solution:
        
    def helper(self, ans, path, nums):
        if not nums:
            ans.append(path)
            
        for i in range(len(nums)):
            self.helper(ans, path + [nums[i]], nums[0:i] + nums[i+1:len(nums)])

    
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        self.helper(ans, [], nums)
        
        return ans
        
                