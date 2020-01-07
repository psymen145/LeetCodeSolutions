class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # trivial solution hash table
        '''
        hash_tbl = {}
        for num in nums:
            if num not in hash_tbl:
                hash_tbl[num] = 1
            else:
                hash_tbl[num] += 1
                
        for key, value in hash_tbl.items():
            if value != 2:
                return key
        '''
        a = 0
        for num in nums:
            a = a ^ num
            
        return a