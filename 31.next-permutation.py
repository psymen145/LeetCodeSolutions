class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        set_point = None
        for i in range(len(nums)-1, -1, -1):
            if (i-1) >= 0 and nums[i-1] < nums[i]:
                set_point = i - 1
                break
            elif i == 0:
                return nums.sort()
        
        # find the next largest integer from set_pt index and greater
        next_largest = 99999999
        next_largest_index = i
        for i in range(set_point+1, len(nums)):
            if nums[i] > nums[set_point] and nums[i] < next_largest:
                next_largest = nums[i]
                next_largest_index = i
        
        # swapping
        tmp = nums[set_point]
        nums[set_point] = next_largest
        nums[next_largest_index] = tmp
        
        # sort the right hand side of the setpoint
        nums[set_point+1:] = sorted(nums[set_point+1:])