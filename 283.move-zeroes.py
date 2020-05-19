class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # everytime we encounter non zero, move it to the "front"
        # front as in, one element after the non zero number
        # then the rest of the array will need to be filled with zero

        # run time should be n

        p1 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p1] = nums[i]
                p1 += 1
                
        for i in range(p1, len(nums)):
            nums[i] = 0
                
        