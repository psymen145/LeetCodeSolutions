class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # trivial way, sort it.
        
        # for each i :
        # put in hash table
        # use the given lenght of nums
        # loop through entire 
        
        longest_str = 0
        set_nums = set(nums)
        
        for i in range(len(nums)):
            if nums[i] - 1 in set_nums:
                continue
                
            tmp_longest = 0
            curr_num = nums[i]
            while curr_num in set_nums:
                tmp_longest += 1
                curr_num += 1
                
            longest_str = max(longest_str, tmp_longest)
            
        return longest_str 