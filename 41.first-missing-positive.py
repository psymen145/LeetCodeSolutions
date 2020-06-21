class Solution:
    """
    def _firstMissingPositive(self, nums: List[int]) -> int:
                
        # trivial, sort the list
        if not nums:
            return 1
        
        nums.sort()
        
        # loop through 1 and max number in array
        max_num = nums[-1]
        
        if max_num < 1:
            return 1
        
        # put numbers into a hashtbl
        hashtbl = {}
        for n in nums:
            hashtbl[n] = True
        
        # first number to be missing will be the smallest missing
        for i in range(1, max_num):
            if i not in hashtbl:
                return i
        
        return max_num + 1
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = 0
        
        hashtbl = {}
        for n in nums:
            if n > max_num:
                max_num = n
                
            hashtbl[n] = True
            
        if max_num < 0:
            return 1
        
        for i in range(1, max_num):
            if i not in hashtbl:
                return i
            
        return max_num + 1