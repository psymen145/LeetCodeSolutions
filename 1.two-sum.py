class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # one pass hash table
        hash_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in hash_table:
                return [i, hash_table[complement]]
            
            hash_table[nums[i]] = i