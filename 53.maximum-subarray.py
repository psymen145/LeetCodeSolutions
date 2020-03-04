class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        whole_arr_max = sub_arr_max = nums[0]
        
        for i in range(1, len(nums)):
            sub_arr_max = max(nums[i], sub_arr_max + nums[i])
            
            whole_arr_max = sub_arr_max if sub_arr_max > whole_arr_max else whole_arr_max
            
        return whole_arr_max