class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort the array, find the number that is at n/2
        elem_to_check = len(nums) // 2
        
        nums.sort()
        
        return nums[elem_to_check]