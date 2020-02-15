#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # loop through once (keeping pointer to current location)
        # if number is val, then look at next number, if not val...
        # move to current pointer. If it is val, move second pointer and repeat second step

        len_new = 0
        j = 0
        for i in range(len(nums)):
            while j < len(nums):
                if val != nums[j]:
                    nums[i] = nums[j]
                    len_new += 1
                    j += 1
                    continue

                j += 1

                if j == len(nums):
                    print(len_new)
                    return len_new
                

# @lc code=end

