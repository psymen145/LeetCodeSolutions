class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # trivial solution, one single pass O(n)
        # for i in range(len(nums)):
        #    if nums[i] >= target:
        #        return i  
        # return len(nums)
        
        # non trivial solution, use binary search?
        if len(nums) == 0:
            return
        
        first = 0
        last = len(nums) - 1
        
        while first <= last:
            middle = (first + last) // 2
            
            if nums[middle] < target:
                first = middle + 1
            elif nums[middle] > target:
                last = middle - 1
            else:
                return middle
                
        return first
            
            
                