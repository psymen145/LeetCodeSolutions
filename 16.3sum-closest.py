class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # trivial O(n^3)
        '''
        #nums.sort()
        length_of_nums = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(length_of_nums-2):
            for l in range(i + 1, length_of_nums-1):
                for r in range(l + 1, length_of_nums):
                    s = nums[i] + nums[l] + nums[r] 

                    if s == target:
                        return s

                    if abs(target-s) < abs(target-closest_sum):
                        closest_sum = s
                
        return closest_sum
        '''
        
        nums.sort()
        length_of_nums = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(length_of_nums-2):
            l = i + 1
            r = length_of_nums - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                if s == target:
                    return s
                
                if abs(target-s) < abs(target-closest_sum):
                    closest_sum = s
                    
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                
                
        return closest_sum
                